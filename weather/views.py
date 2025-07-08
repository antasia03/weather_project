import requests
from django.shortcuts import render
from .models import WeatherQuery
from decouple import config
from django.utils.timezone import now
from .forms import CityForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def weather_view(request):
    error = None
    form = CityForm(request.POST or None)
    weather_data = None

    if request.method == 'POST' and form.is_valid():
        city = form.cleaned_data['city']
        api_key = config('OPENWEATHER_API_KEY')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            description = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            WeatherQuery.objects.create(
                city=city,
                temperature=temp,
                feels_like=feels_like,
                humidity=humidity,
                pressure=pressure,
                wind_speed=wind_speed,
                description=description,
                timestamp=now(),
            )

            weather_data = {
                'city': city,
                'temperature': temp,
                'feels_like': feels_like,
                'humidity': humidity,
                'pressure': pressure,
                'wind_speed': wind_speed,
                'description': description,
            }

    history_list = WeatherQuery.objects.order_by('-timestamp')
    paginator = Paginator(history_list, 10)  # 10 записей на страницу

    page = request.GET.get('page')  # получаем номер страницы из GET-параметров
    try:
        history = paginator.page(page)
    except PageNotAnInteger:
        history = paginator.page(1)
    except EmptyPage:
        history = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {
        'form': form,
        'history': history,
        'error': error,
        'weather_data': weather_data,
    })
