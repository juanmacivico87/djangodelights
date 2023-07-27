from django.core.exceptions import ValidationError
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=10)
    price_per_unit = models.FloatField(default=0.0)
    
    def __str__(self):
        return f'{self.name} ({self.quantity} {self.unit})'
    
    def clean(self):
        if self.quantity < 0:
            raise ValidationError('You cannot have an ingredient with an amount less than zero.')
        
        if self.price_per_unit < 0:
            raise ValidationError('You cannot have an ingredient with a price per unit less than zero.')