from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _

class Ingredient(models.Model):
    name = models.CharField(_('Ingredient'), max_length=20)
    quantity = models.FloatField(_('Quantity'), default=0.0)
    unit = models.CharField(_('Unit'), max_length=10)
    price_per_unit = models.FloatField(_('Price per Unit'), default=0.0)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        if self.quantity < 0:
            raise ValidationError(_('You cannot have an ingredient with an amount less than zero.'))
        
        if self.price_per_unit < 0:
            raise ValidationError(_('You cannot have an ingredient with a price per unit less than zero.'))
        
    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')