from django.db import models


# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField('myapp/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Forblog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title
