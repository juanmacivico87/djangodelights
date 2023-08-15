from django.contrib import admin

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'menu_item', 'user', 'timestamp']
    list_filter = [
        ('user', admin.RelatedOnlyFieldListFilter),
        ('menu_item', admin.RelatedOnlyFieldListFilter),
    ]
