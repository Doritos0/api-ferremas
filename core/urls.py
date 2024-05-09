from django.urls import path
from .views import lista_productos, detalle_producto, lista_tipos, detalle_tipo, lista_clientes, detalle_cliente, lista_pedidos, detalle_pedido

urlpatterns=[
    path('lista_productos/',lista_productos, name="lista_productos"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('lista_tipos/',lista_tipos, name="lista_tipos"),
    path('detalle_tipo/<id>', detalle_tipo, name="detalle_tipo"),
    path('lista_clientes/',lista_clientes, name="lista_clientes"),
    path('detalle_cliente/<rut>', detalle_cliente, name="detalle_cliente"),
    path('lista_pedidos/',lista_pedidos, name="lista_pedidos"),
    path('detalle_pedido/<id>', detalle_pedido, name="detalle_pedido"),
]