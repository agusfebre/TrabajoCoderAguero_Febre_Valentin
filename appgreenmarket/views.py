from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Proveedor, Cliente
from .forms import ProductoForm, ProveedorForm, ClienteForm

# Create your views here.

def inicio(request):
    return render (request, "inicio.html")

def cargaProducto(request):
    if request.method=="POST":
        form= ProductoForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            codigo= info["codigo"]
            nombre= info["nombre"]
            marca= info["marca"]
            tipo= info["tipo"]
            cantidad= info["cantidad"]
            precio= info["precio"]
            product= Producto(codigo=codigo, nombre=nombre, marca=marca, tipo=tipo, cantidad=cantidad, precio=precio)
            product.save()
            return render (request, "cargaProducto.html", {"mensaje": "Producto Cargado Exitosamente!"})
        else:
            return render (request, "cargaProducto.html", {"mensaje": "Error en carga de producto"})
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
            return render (request, "cargaProveedor.html", {"mensaje": "Se cargó el Proveedor!"})
        else:
            return render (request, "cargaProveedor.html", {"mensaje": "Error en la carga de Proveedor"})
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
            cliente= Cliente(nombre=nombre, apellido=apellido, fechaNacimiento=fechaNacimiento, direccion=direccion, telefono=telefono, email=email)
            cliente.save()
            return render (request, "cargaCliente.html", {"mensaje": "El cliente se agregó a la base de datos!"})
        else:
            return render (request, "cargaCliente.html", {"mensaje": "Error en la carga del cliente"})
    else:
        form= ClienteForm()
    return render(request, "cargaCliente.html", {"formulario":form})


    ## Lista de Productos
def listaProductos(request):
    productos=Producto.objects.all()
    print(productos)
    return render(request, "listadoProductos.html", {"productos":productos})


#buscar
def busquedaProducto(request):
    return render(request, "busquedaProducto.html")

def buscar(request):
    if request.GET["codigo"]:
        producto=request.GET["codigo"]
        productos=Producto.objects.filter(codigo=producto)
        if len(productos)!=0:
            return render(request, "resultadosBusqueda.html", {"productos":productos})
        else:
            return render(request, "resultadosBusqueda.html", {"mensaje": "No hay productos"})
    else:
        return render(request, "busquedaProducto.html", {"mensaje": "No enviaste datos!"})
