from django.contrib import admin
from .models import Ingredient,Table,Dish,Category

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Table)
admin.site.register(Dish)
admin.site.register(Category)