from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views import View
from inventory.models.ingredient import Ingredient as IngredientModel

class Ingredient(View):
    def get(self, request):
        ingredients = IngredientModel.objects.all()
        
        if not ingredients:
            return JsonResponse([], status=200, safe=False)
        
        data = [{
            'name': ingredient.name,
            'quantity': ingredient.quantity,
            'unit': ingredient.unit,
            'price_per_unit': ingredient.price_per_unit
        } for ingredient in ingredients]
        
        return JsonResponse(data, status=200, safe=False)