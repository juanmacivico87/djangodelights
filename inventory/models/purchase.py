from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from inventory.models.menuItem import MenuItem

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Date', default=timezone.now)
    
    def __str__(self):
        return f'#{self.id}'
    
    def update_ingredients_quantities(self, recipe_requeriments):
        for item in recipe_requeriments:
            item.ingredient.quantity -= item.quantity
            item.ingredient.save()
    
    def clean(self):
        if self.timestamp > timezone.now():
            raise ValidationError('The date of purchase cannot exceed the current date.')
        
        recipe_requeriments = self.menu_item.reciperequirement_set.all()
        
        if self.pk is not None:
            return
        
        for item in recipe_requeriments:
            quantity = item.quantity
            ingredient_quantity = item.ingredient.quantity
            
            if ingredient_quantity < quantity:
                ingredient = item.ingredient.name
                unit = item.ingredient.unit
                raise ValidationError(f'To prepare {self.menu_item} you need {quantity} {unit} of {ingredient} and you only have {ingredient_quantity} {unit} in your inventory.')
            
        self.update_ingredients_quantities(recipe_requeriments)

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'