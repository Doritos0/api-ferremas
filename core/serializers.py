from rest_framework import serializers
from .models import Productos, TipoProducto

class ProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class TipoProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'