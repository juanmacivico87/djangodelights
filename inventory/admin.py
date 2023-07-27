from django.contrib import admin
from inventory.models.ingredient import Ingredient
from inventory.models.menuItem import MenuItem
from inventory.models.recipeRequirement import RecipeRequirement

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)