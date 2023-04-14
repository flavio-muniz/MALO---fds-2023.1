from django import forms
from django.forms import ModelForm
from .models import Ingredient,Dish

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name','exp_date','quantity','measure_unit','price','obs')

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ('name','price','description','ingredients')

