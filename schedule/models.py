from django.db import models


# Create your models here.
class Amperage(models.Model):
    cargo = models.IntegerField()
    operation = models.IntegerField()
    axis = models.IntegerField()
    value = models.DecimalField(max_digits=20, decimal_places=14)
