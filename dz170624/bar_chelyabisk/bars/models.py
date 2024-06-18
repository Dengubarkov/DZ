from django.db import models

class Bars(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='bars/images/')
    url = models.URLField(blank=True)
    star = models.CharField(max_length=2)
