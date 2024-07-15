from django.contrib import admin
from .models import Producto, TipoProducto, Usuario, Pedido, Stock, Precio#, Oferta

# Register your models here.

admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(Stock)
admin.site.register(Precio)
#admin.site.register(Oferta)
