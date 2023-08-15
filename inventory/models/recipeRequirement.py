from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _
from inventory.models.ingredient import Ingredient
from inventory.models.menuItem import MenuItem

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, verbose_name=_('Menu Item'))
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name=_('Ingredient'))
    quantity = models.FloatField(_('Quantity'), default=0.0)
    
    def __str__(self):
        return f'#{self.id}'
    
    def clean(self):
        if self.quantity < 0:
            raise ValidationError(_('You cannot have a recipe requirement with a quantity less than zero.'))
        
    class Meta:
        verbose_name = _('Recipe Requirement')
        verbose_name_plural = _('Recipe Requirements')