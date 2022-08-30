from django.shortcuts import render
from django.template import Template
from django.http import HttpResponse
from .models import *
from appgreenmarket import ProductoForm, ProveedorForm

# Create your views here.

def inicio(request):
    return render (request, "inicio.html")

def cargaProducto(request):
    if request.method=="POST":
        form= ProductoForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            marca= info["marca"]
            tipo= info["tipo"]
            precio= info["precio"]
            product= Producto(nombre=nombre, marca=marca, tipo=tipo, precio=precio)
            product.save()
            return render (request, "inicio.html", {"mensaje": "Producto Cargado Exitosamente!"})
        else:
            return render (request, "inicio.html", {"mensaje": "Error en carga de producto"})
    else:
        form= ProductoForm()
    return render(request, "cargaProducto.html", {"formulario":form})


def cargaProveedor(request):
    if request.method=="POST":
        form= ProveedorForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            direccion= info["direccion"]
            telefono= info["telefono"]
            email= info["email"]
            proveedor= Proveedor(nombre=nombre, direccion=direccion, telefono=telefono, email=email)
            proveedor.save()
            return render (request, "inicio.html", {"mensaje": "Se cargó el Proveedor!"})
        else:
            return render (request, "inicio.html", {"mensaje": "Error en la carga de Proveedor"})
    else:
        form= ProveedorForm()
    return render(request, "cargaProveedor.html", {"formulario":form})