from django.shortcuts import render, redirect
from .forms import *
from gestion.models import Producto
from .utils.verificar_credenciales import verificar_credenciales
from .utils.redireccion import *
from django.contrib import messages


def listadoProductos(request):
    productos = Producto.objects.all()

    return render(request, 'producto/lista.html', {'productos': productos})


def agregarProducto(request):
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/productos/')

    else:
        form = FormProducto()

    return render(request, 'producto/agregar.html', {'form': form})


def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/productos')


def actualizarProducto(request, id):
    productos = Producto.objects.get(id=id)
    form = FormProducto(instance=productos)
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=productos)
        if form.is_valid():
            form.save()
        return listadoProductos(request)

    return render(request, 'producto/agregar.html', {'form': form})


# CRUD boleta
def listadoBoleta(request):
    facturas = Detalle_boleta.objects.all()

    return render(request, 'boleta/lista.html', {'facturas': facturas})


def agregarBoleta(request):
    if request.method == 'POST':
        form = FormFactura(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/facturas/')

    else:
        form = FormFactura()

    return render(request, 'boleta/agregar.html', {'form': form})


def actualizarBoleta(request, numero_boleta):
    facturas = Detalle_boleta.objects.get(numero_boleta=numero_boleta)
    form = FormFactura(instance=facturas)
    if request.method == 'POST':
        form = FormFactura(request.POST, instance=facturas)
        if form.is_valid():
            form.save()
        return listadoBoleta(request)

    return render(request, 'boleta/agregar.html', {'form': form})


# CRUD factura

def listadoFactura(request):
    facturas = Detalle_factura.objects.all()

    return render(request, 'facturas/lista.html', {'facturas': facturas})


def agregarFactura(request):
    if request.method == 'POST':
        form = FormFactura(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/facturas/')

    else:
        form = FormFactura()

    return render(request, 'facturas/agregar.html', {'form': form})


def actualizarFactura(request, nro_factura):
    facturas = Detalle_boleta.objects.get(nro_factura=nro_factura)
    form = FormFactura(instance=facturas)
    if request.method == 'POST':
        form = FormFactura(request.POST, instance=facturas)
        if form.is_valid():
            form.save()
        return listadoBoleta(request)

    return render(request, 'facturas/agregar.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']
            if verificar_credenciales(rut, password):
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('facturas/agregar.html')  # Reemplaza 'inicio' con la ruta a donde quieras redirigir al usuario
            else:
                messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
