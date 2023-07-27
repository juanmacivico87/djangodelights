from django.core.exceptions import ValidationError
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0.0)
    
    def __str__(self):
        return f'{self.title}'
    
    def clean(self):
        if self.price < 0:
            raise ValidationError('You cannot have a menu item with a price less than zero.')