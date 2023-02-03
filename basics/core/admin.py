from django.contrib import admin
from .models import Product

# create a class to add information on admin page
class ProductAdminView(admin.ModelAdmin):
    list_display = ('name', 'price')

# Register your models here.
admin.site.register(Product, ProductAdminView)

# here, we can registrate models
# this models can be access in django admin