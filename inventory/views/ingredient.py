from django.utils.translation import gettext as _
from django.views import View
from inventory.models.ingredient import Ingredient as IngredientModel
from inventory import helpers

class Ingredient(View):
    create_path = 'ingredients/create/'
    list_path = 'ingredients/list/'
    single_path = 'ingredients/<int:id>/'
    update_path = 'ingredients/update/<int:id>/'
    delete_path = 'ingredients/delete/<int:id>/'
    
    def get_ingredient_data(self, ingredient):
        return {
            'id': ingredient.id,
            'name': ingredient.name,
            'quantity': ingredient.quantity,
            'unit': ingredient.unit,
            'price_per_unit': ingredient.price_per_unit
        }
    
    def get_all_ingredients(self):
        ingredients = IngredientModel.objects.all()
        data = [self.get_ingredient_data(ingredient) for ingredient in ingredients]
        
        return helpers.get_response(200, data)
        
    def get_ingredient(self, id):
        ingredient = IngredientModel.objects.get(id=id)
        data = [self.get_ingredient_data(ingredient)]
        
        return helpers.get_response(200, data)
    
    def get(self, request, id = 0):
        if request.path_info == helpers.format_url(self.list_path, '', '', '/api'):
            return self.get_all_ingredients()
        
        if request.path_info == helpers.format_url(self.single_path, '<int:id>', id, '/api'):
            return self.get_ingredient(id)
        
        return helpers.get_response(404, [], _('Error: Route not found'))