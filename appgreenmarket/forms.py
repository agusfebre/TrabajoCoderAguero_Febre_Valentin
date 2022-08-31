from django import forms

class ProductoForm(forms.Form):
    codigo=forms.IntegerField()
    nombre=forms.CharField(max_length=50)
    marca=forms.CharField(max_length=50)
    tipo=forms.CharField(max_length=50)
    precio=forms.IntegerField()

class ProveedorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    direccion=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
    email=forms.EmailField()

class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    fechaNacimiento=forms.DateField()
    direccion=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
    email=forms.EmailField()