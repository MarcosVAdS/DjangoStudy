from django.db import models

# Create your models here.
# model describe a model of data to our project
# when decriobe a class, we create a model of data 
# that will be used and saved on database
class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Stock')

    # when object is called return his name
    def __str__(self):
        return self.name

# class Product describe a model data called product
# for every model, python creates migratiions
# each migration has a number indentifier, for migration version
# migration describes what model is, like, tipe, name, type of data,
# and more

# python makemigrations create a migrations file for each model update
# python migrate apply migrations to database