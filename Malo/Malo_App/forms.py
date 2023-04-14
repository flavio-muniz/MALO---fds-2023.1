from django import forms
from django.forms import ModelForm
from .models import Ingredient,Dish, Category

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name','exp_date','quantity','measure_unit','price','obs')

class DishForm(ModelForm):
    class Meta:
        model = Category
        model = Dish
        fields = ('name','price','description','ingredients')

