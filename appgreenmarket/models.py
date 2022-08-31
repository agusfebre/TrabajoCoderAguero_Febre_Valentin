from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    precio=models.FloatField()

class Proveedor(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()
