from rest_framework import serializers
from .models import Productos, TipoProducto, Cliente, Pedido

class ProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class TipoProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoSerializer (serializers.ModelSerializer):
    fecha_pedido = serializers.DateField(format="%d/%m/%Y")
    class Meta:
        model = Pedido
        fields = '__all__'