from django.core.exceptions import ValidationError
from django.db import models
from inventory.models.ingredient import Ingredient
from inventory.models.menuItem import MenuItem

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    
    def __str__(self):
        return f'{self.menu_item} - {self.ingredient}'
    
    def clean(self):
        if self.quantity < 0:
            raise ValidationError('You cannot have a recipe requirement with a quantity less than zero.')