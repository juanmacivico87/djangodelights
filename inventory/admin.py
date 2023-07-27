from django.contrib import admin
from inventory.models.ingredient import Ingredient
from inventory.models.menuItem import MenuItem

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)