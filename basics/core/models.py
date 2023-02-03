from django.db import models

# Create your models here.
# model describe a model of data to our project
# when decriobe a class, we create a model of data 
# that will be used and saved on database
class Product(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')

# class Product describe a model data called product
# for every model, python creates migratiions
# each migration has a number indentifier, for migration version
# migration describes what model is, like, tipe, name, type of data,
# and more