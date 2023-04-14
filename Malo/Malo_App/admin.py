from django.contrib import admin
from .models import Ingredient,Mesa,Dish,Category

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Mesa)
admin.site.register(Dish)
admin.site.register(Category)