"""TDA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestion.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    #productos
    path('productos/',listadoProductos),
    path('agregarProducto/',agregarProducto),
    path('eliminarProducto/<int:id>',eliminarProducto),
    path('actualizarProducto/<int:id>',actualizarProducto),
    #boletas
    path('boletas/',listadoBoleta),
    path('agregarBoleta/',agregarBoleta),
    path('actualizarBoleta/<int:numero_boleta>',actualizarBoleta),
    #facturas
    path('facturas/',listadoFactura),
    path('agregarFactura/',agregarFactura),
    path('actualizarFactura/<int:nro_factura>',actualizarFactura)
]
