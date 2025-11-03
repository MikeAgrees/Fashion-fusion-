from django.contrib import admin
from .models import *

class ProductStockAdmin(admin.ModelAdmin):
    # Define how the model should be displayed in the admin interface
    list_display = ('id','name', 'price', 'image')

# Register the model with the admin site
admin.site.register(ProductStock, ProductStockAdmin)
