from django import forms
from django.forms import ModelForm
from .models import Ingredient, Dish, Category, DishIngredient, Order

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name','exp_date','quantity','measure_unit','price','obs')

        labels = {
            'name':'Nome:',
            'exp_date':'Data de validade(aaaa-mm-dd):',
            'quantity':'Quantidade',
            'measure_unit':'Unidade de medida( Ex.: kg,gramas,litros,ml,unidades,etc)',
            'price':'Preço de compra:',
            'obs':'Observação:',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}),
            'exp_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Data de validade'}),
            'quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantidade'}),
            'measure_unit': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidade de medida'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Preço'}),
            'obs': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observação:'}),
        }

class DishIngredientForm(ModelForm):
    class Meta:
        model = DishIngredient
        fields = ('name','quantity','measure_unit')

        labels = {
            'name':'Nome:',
            'quantity':'Quantidade',
            'measure_unit':'Unidade de medida( Ex.: kg,gramas,litros,ml,unidades,etc)',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}),
            'quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantidade'}),
            'measure_unit': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidade de medida'}),
        }

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('category','name', 'price', 'description')

        labels = {
            'category': 'Categoria:',
            'name': 'Nome do prato:',
            'price': 'Preço:',
            'description': 'Descrição no cardápio:',
        }
        widgets = {
            'category': forms.Select(attrs={'class':'form-control', 'placeholder':'Categoria'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Preço'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição no cardápio'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        
        labels = {
            'name': 'Categoria:',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Categoria'}),
        }

class AddMesaOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('dish',)

        widgets = {
            'dish': forms.CheckboxSelectMultiple(),
        }
