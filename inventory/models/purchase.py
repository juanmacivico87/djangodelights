from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from inventory.models.menuItem import MenuItem

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, verbose_name=_('Menu Item'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    timestamp = models.DateTimeField(_('Date'), default=timezone.now)
    
    def __str__(self):
        return f'#{self.id}'
    
    def update_ingredients_quantities(self, recipe_requeriments):
        for item in recipe_requeriments:
            item.ingredient.quantity -= item.quantity
            item.ingredient.save()
    
    def clean(self):
        if self.timestamp > timezone.now():
            raise ValidationError(_('The date of purchase cannot exceed the current date.'))
        
        recipe_requeriments = self.menu_item.reciperequirement_set.all()
        
        if self.pk is not None:
            return
        
        for item in recipe_requeriments:
            quantity = item.quantity
            ingredient_quantity = item.ingredient.quantity
            
            if ingredient_quantity < quantity:
                raise ValidationError(_('To prepare %(menu_item)s you need %(quantity)s %(unit)s of %(ingredient)s and you only have %(ingredient_quantity)s %(unit)s in your inventory.') % {
                    'menu_item': self.menu_item,
                    'quantity': quantity,
                    'unit': item.ingredient.unit,
                    'ingredient': item.ingredient.name,
                    'ingredient_quantity': ingredient_quantity,
                })
            
        self.update_ingredients_quantities(recipe_requeriments)

    class Meta:
        verbose_name = _('Purchase')
        verbose_name_plural = _('Purchases')