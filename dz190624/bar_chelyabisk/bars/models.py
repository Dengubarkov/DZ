from django.db import models

class Bars(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='bars/images/')
    url = models.URLField(blank=True)
    star = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=400)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title