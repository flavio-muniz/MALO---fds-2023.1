from django import forms
from django.forms import ModelForm
from .models import Ingredient,Dish, Category

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

class DishForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Dish
        fields = ('category', 'name', 'price', 'description', 'ingredients')

        labels = {
            'category': 'Categoria:',
            'name': 'Nome do prato:',
            'price': 'Preço:',
            'description': 'Descrição no cardápio:',
            'ingredients': 'Ingredientes:',
        }
        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Preço'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição no cardápio'}),
            'ingredients': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Ingredientes'}),
        }

    def save(self, commit=True):
        dish = super().save(commit=False)
        category = self.cleaned_data['category']
        dish.save()
        category.dishes.add(dish)
        return dish
