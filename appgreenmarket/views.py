from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Proveedor, Cliente
from .forms import ProductoForm, ProveedorForm, ClienteForm

# Create your views here.

def inicio(request):
    return render (request, "inicio.html")

def cargaProducto(request):
    if request.method=="POST":
        form= CargaForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            codigo= info["codigo"]
            nombre= info["nombre"]
            marca= info["marca"]
            tipo= info["tipo"]
            precio= info["precio"]
            product= Producto(codigo=codigo, nombre=nombre, marca=marca, tipo=tipo, precio=precio)
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

def cargaCliente(request):
    if request.method=="POST":
        form= ClienteForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            fechaNacimiento= info["fechaNacimiento"]
            direccion= info["direccion"]
            telefono= info["telefono"]
            email= info["email"]
            cliente= cliente(nombre=nombre, apellido=apellido, fechaNacimiento=fechaNacimiento, direccion=direccion, telefono=telefono, email=email)
            cliente.save()
            return render (request, "inicio.html", {"mensaje": "El cliente se agregó a la base de datos!"})
        else:
            return render (request, "inicio.html", {"mensaje": "Error en la carga del cliente"})
    else:
        form= ClienteForm()
    return render(request, "cargaCliente.html", {"formulario":form})