from django.urls import path
from .views import lista_productos, detalle_producto, lista_tipo, detalle_tipo

urlpatterns=[
    path('lista_productos/',lista_productos, name="lista_productos"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('lista_tipo/',lista_tipo, name="lista_tipo"),
    path('detalle_tipo/<id>', detalle_tipo, name="detalle_tipo"),
]