from django import forms
from django.forms import ModelForm
from .models import Ingredient, Dish, Category, DishIngredient

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
    Categoria = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Dish
        fields = ('Categoria', 'name', 'price', 'description')

        labels = {
            'Categoria': 'Categoria:',
            'name': 'Nome do prato:',
            'price': 'Preço:',
            'description': 'Descrição no cardápio:',
        }
        widgets = {
            'ategoria': forms.Select(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Preço'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição no cardápio'}),
        }

    def save(self, commit=True):
        dish = super().save(commit=False)
        Categoria = self.cleaned_data['Categoria']
        dish.save()
        Categoria.dishes.add(dish)
        return dish
