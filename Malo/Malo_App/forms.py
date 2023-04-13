from django import forms
from django.forms import ModelForm
from .models import Ingredient

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name','exp_date','quantity','measure_unit','price','obs')

