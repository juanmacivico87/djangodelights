from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=10)
    price_per_unit = models.FloatField(default=0.0)