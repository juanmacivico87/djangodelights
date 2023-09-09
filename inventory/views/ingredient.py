from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views import View
from inventory.models.ingredient import Ingredient as IngredientModel

class Ingredient(View):
    def get_all_ingredients(self):
        ingredients = IngredientModel.objects.all()
        data = [{
            'id': ingredient.id,
            'name': ingredient.name,
            'quantity': ingredient.quantity,
            'unit': ingredient.unit,
            'price_per_unit': ingredient.price_per_unit
        } for ingredient in ingredients]
        
        response = {
            'num_items': len(data),
            'data': data,
        }
        
        return JsonResponse(response, status=200, safe=False)
        
    def get_ingredient(self, id):
        ingredient = IngredientModel.objects.get(id=id)
        data = [{
            'id': ingredient.id,
            'name': ingredient.name,
            'quantity': ingredient.quantity,
            'unit': ingredient.unit,
            'price_per_unit': ingredient.price_per_unit
        }]
        
        response = {
            'num_items': len(data),
            'data': data,
        }
        
        return JsonResponse(response, status=200, safe=False)