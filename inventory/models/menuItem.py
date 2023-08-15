from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _

class MenuItem(models.Model):
    title = models.CharField(_('Menu Item'), max_length=20)
    price = models.FloatField(_('Price'), default=0.0)
    
    def __str__(self):
        return self.title
    
    def clean(self):
        if self.price < 0:
            raise ValidationError(_('You cannot have a menu item with a price less than zero.'))
        
    class Meta:
        verbose_name = _('Menu Item')
        verbose_name_plural = _('Menu Items')