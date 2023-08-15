from django.contrib import admin

class RecipeRequirementAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'ingredient', 'menu_item']
    list_filter = [
        ('ingredient', admin.RelatedOnlyFieldListFilter),
        ('menu_item', admin.RelatedOnlyFieldListFilter),
    ]
