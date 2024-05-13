from rest_framework import serializers
from .models import Producto, TipoProducto, Cliente, Pedido, Stock

class ProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Producto
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

class StockSerializer (serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'