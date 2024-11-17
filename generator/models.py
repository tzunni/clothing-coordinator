from django.db import models

class Weather(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Shade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE)
    shade = models.ForeignKey(Shade, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
