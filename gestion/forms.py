from django import forms
from .models import *

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','marca','stock','unidad_medida','precio','codigo_barra']


class FormBoleta(forms.ModelForm):
    class Meta:
        model = Detalle_boleta
        fields = ['direccion_venta','cantidad','monto','nombre','estado']


class FormFactura(forms.ModelForm):
    class Meta:
        model = Detalle_factura
        fields = ['sitio_compra','nombre_producto','cantidad','precio','proveedor','estado']

class LoginForm(forms.Form):
    rut = forms.CharField(label='RUT', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())