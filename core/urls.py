from django.urls import path
from .views import lista_productos, detalle_producto, lista_tipos, detalle_tipo, lista_usuarios, detalle_usuario, lista_pedidos, detalle_pedido, lista_stocks, detalle_stock, lista_precios, detalle_precio#, lista_ofertas, detalle_oferta

urlpatterns=[
    path('lista_productos/',lista_productos, name="lista_productos"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('lista_tipos/',lista_tipos, name="lista_tipos"),
    path('detalle_tipo/<id>', detalle_tipo, name="detalle_tipo"),
    path('lista_usuarios/',lista_usuarios, name="lista_usuarios"),
    path('detalle_usuario/<user>', detalle_usuario, name="detalle_usuario"),
    path('lista_pedidos/',lista_pedidos, name="lista_pedidos"),
    path('detalle_pedido/<id>', detalle_pedido, name="detalle_pedido"),
    path('lista_stocks/',lista_stocks, name="lista_stocks"),
    path('detalle_stock/<id>', detalle_stock, name="detalle_stock"),
    path('lista_precios/',lista_precios, name="lista_precios"),
    path('detalle_precio/<id>', detalle_precio, name="detalle_precio"),
    #path('lista_ofertas/',lista_ofertas, name="lista_ofertas"),
    #path('detalle_oferta/<id>', detalle_oferta, name="detalle_oferta"),
]