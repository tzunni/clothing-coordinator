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
    TYPE_CHOICES = [
        ('Top', 'Top'),
        ('Bottom', 'Bottom'),
        ('Accessory', 'Accessory'),
    ]
    name = models.CharField(max_length=100)
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE)
    shade = models.ForeignKey(Shade, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Top')

    def __str__(self):
        return self.name
