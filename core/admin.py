from django.contrib import admin
from .models import Productos, TipoProducto

# Register your models here.

admin.site.register(TipoProducto)
admin.site.register(Productos)
