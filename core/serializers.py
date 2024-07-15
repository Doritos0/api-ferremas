from rest_framework import serializers
from .models import Producto, TipoProducto, Usuario, Pedido, Stock, Precio#, Oferta

class ProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class TipoProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
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

class PrecioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = '__all__'

'''
class OfertaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'


'''