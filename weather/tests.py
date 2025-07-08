from django.test import TestCase, Client
from django.urls import reverse
from .models import WeatherQuery
from .forms import CityForm
from unittest.mock import patch
from django.utils.timezone import now


class WeatherQueryModelTest(TestCase):
    def test_create_weather_query(self):
        query = WeatherQuery.objects.create(
            city='London',
            temperature=20.5,
            feels_like=18.0,
            humidity=65,
            pressure=1013,
            wind_speed=4.5,
            description='clear sky',
            timestamp=now()
        )
        self.assertEqual(query.city, 'London')
        self.assertEqual(query.temperature, 20.5)


class WeatherViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_get_weather_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Weather")

    @patch('weather.views.requests.get')
    def test_post_valid_city(self, mock_get):
        mock_response = {
            'main': {
                'temp': 22.0,
                'feels_like': 21.0,
                'humidity': 60,
                'pressure': 1012
            },
            'weather': [{'description': 'sunny'}],
            'wind': {'speed': 3.2}
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = self.client.post(self.url, data={'city': 'Paris'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(WeatherQuery.objects.filter(city='Paris').exists())


class CityFormTest(TestCase):
    def test_valid_form(self):
        form = CityForm(data={'city': 'Tokyo'})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = CityForm(data={'city': ''})
        self.assertFalse(form.is_valid())
