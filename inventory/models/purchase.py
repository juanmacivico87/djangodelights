from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from inventory.models.menuItem import MenuItem

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f'#{self.id}'
    
    def clean(self):
        if self.timestamp > timezone.now():
            raise ValidationError('The date of purchase cannot exceed the current date.')