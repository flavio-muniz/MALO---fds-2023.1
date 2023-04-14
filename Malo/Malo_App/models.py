from django.db import models
from django.core.validators import MinValueValidator



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

class Dish(models.Model):
    name = models.CharField('Nome do prato', max_length=120)
    '''Nome do prato'''
    price = models.FloatField('Preço de venda')
    '''Preço do prato'''
    description = models.TextField('Descrição')
    '''Descrição do prato'''
    ingredients = models.ManyToManyField(Ingredient)
    '''Ingredientes utilizados no prato'''

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('Categoria', max_length=120)
    '''Nome da categoria'''
    dishes = models.ManyToManyField(Dish, blank=True)
    '''Pratos na categoria'''

    def __str__(self):
        return self.name  
   
class Table(models.Model):
    nome = models.CharField(verbose_name='Mesa', max_length=50)

    @classmethod
    def adicionar_mesa(cls, quantidade=1):
        for i in range(quantidade):
            mesa = cls.objects.create(nome=f"Mesa {cls.objects.count() + 1}")
        return mesa

    @classmethod
    def remover_mesa(cls):
        mesa = cls.objects.last()
        mesa.delete()
        return mesa

    def __str__(self):
        return self.nome



    