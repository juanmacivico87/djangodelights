from django.contrib import admin
from inventory.dashboard.ingredient import IngredientAdmin
from inventory.dashboard.purchase import PurchaseAdmin
from inventory.dashboard.recipeRequirement import RecipeRequirementAdmin
from inventory.models.ingredient import Ingredient
from inventory.models.menuItem import MenuItem
from inventory.models.purchase import Purchase
from inventory.models.recipeRequirement import RecipeRequirement

# Register your models here.
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement, RecipeRequirementAdmin)
admin.site.register(Purchase, PurchaseAdmin)