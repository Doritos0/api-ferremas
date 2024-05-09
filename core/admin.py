from django.contrib import admin
from .models import Productos, TipoProducto, Cliente, Pedido

# Register your models here.

admin.site.register(TipoProducto)
admin.site.register(Productos)
admin.site.register(Cliente)
admin.site.register(Pedido)
