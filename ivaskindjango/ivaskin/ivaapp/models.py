from django.db import models


# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField('ivaapp/images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Forclient(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField('ivaapp/images/')
    dopinfo1 = models.CharField(max_length=250, blank=True, null=True)
    dopinfo2 = models.CharField(max_length=250, blank=True, null=True)
    dopinfo3 = models.CharField(max_length=250, blank=True, null=True)
    dopinfo4 = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title
