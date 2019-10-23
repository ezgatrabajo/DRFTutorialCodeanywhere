from django.db import models

# Create your models here.

class Categoria(models.Model):
    name        = models.CharField(max_length=75)
    description = models.CharField(max_length=200)

class Marca(models.Model):
    name        = models.CharField(max_length=75)
    description = models.CharField(max_length=200)