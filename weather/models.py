from django.db import models


class WeatherQuery(models.Model):
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    description = models.CharField(max_length=250)
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    wind_speed = models.FloatField()
    feels_like = models.FloatField()

    def __str__(self):
        return f'{self.city} — {self.temperature}°C, {self.description}'
