from django.contrib import admin

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit']
