from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField('Ingrediente', max_length=120) 
    '''nome do ingrediente'''
    exp_date = models.DateField('Data de validade') 
    '''data de validade'''
    quantity = models.FloatField('Quantidade') 
    '''quantidade que consta no estoque do ingrediente'''
    measure_unit = models.CharField('Unidade de medida',max_length=10) 
    '''unidade de medida utilzada ex.: kg, gramas, etc'''
    price = models.FloatField('Preço de compra(total)')
    '''preco de compra do ingrediente (total)'''
    obs = models.TextField('Observação', blank=True)
    '''ex.: marca parmalate, deixar na geladeira, etc'''

    def __str__(self):
        return self.name

    
    
    
