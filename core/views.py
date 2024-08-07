import json
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import redirect, render

# CREACION DE API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

#IMPORTAMOS EL MODELO
from .models import Producto, TipoProducto, Usuario, Pedido, Stock, Precio#, Oferta
from .serializers import ProductoSerializer, TipoProductoSerializer, UsuarioSerializer, PedidoSerializer, StockSerializer, PrecioSerializer#, OfertaSerializer

# Create your views here.


#TABLA PRODUCTOS API
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_productos (request):
    if request.method == 'GET':
        query = Producto.objects.all()
        serializer = ProductoSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data = request.data)
        print("❤️ ", serializer)
        if serializer.is_valid():
            id = request.POST.get('id_producto', None)
            print(id)
            if id in Producto.objects.values_list('id_producto', flat=True):
                print("💙 ESTE PRODUCTO YA HA SIDO INGRESADO")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH','DELETE'])
def detalle_producto (request,id):
    try:
        producto = Producto.objects.get(id_producto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = ProductoSerializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


#API TABLA TIPO_PRODUCTO
@api_view(['GET', 'POST'])
def lista_tipos(request):
    if request.method == 'GET':
        query = TipoProducto.objects.all()
        serializer = TipoProductoSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TipoProductoSerializer(data=request.data)
        if serializer.is_valid():
            if id in TipoProducto.objects.values_list('id_tipo', flat=True):
                print("💙 ESTE TIPO YA HA SIDO INGRESADO")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "💙 Método no permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','PATCH','DELETE'])
def detalle_tipo (request,id):
    try:
        tipo = TipoProducto.objects.get(id_tipo=id)
    except TipoProducto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TipoProductoSerializer(tipo)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = TipoProductoSerializer(tipo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        tipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
#API TABLA CLIENTE
@api_view(['GET', 'POST'])
def lista_usuarios (request):
    if request.method == 'GET':
        query = Usuario.objects.all()
        serializer = UsuarioSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsuarioSerializer(data = request.data)
        print("❤️ ", serializer)
        if serializer.is_valid():
            id = request.POST.get('user', None)
            print(id)
            if id in Usuario.objects.values_list('user', flat=True):
                print("💙 ESTE PRODUCTO YA HA SIDO INGRESADO")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PATCH','DELETE'])
def detalle_usuario (request,user):
    try:
        cliente = Usuario.objects.get(user=user)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UsuarioSerializer(cliente)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = UsuarioSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#API TABLA PEDIDO
@api_view(['GET', 'POST'])
def lista_pedidos (request):
    if request.method == 'GET':
        query = Pedido.objects.all()
        serializer = PedidoSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PedidoSerializer(data = request.data)
        print("❤️ ", serializer)
        if serializer.is_valid():
            id = request.POST.get('id_pedido', None)
            print(id)
            if id in Pedido.objects.values_list('id_pedido', flat=True):
                print("💙 ESTE PRODUCTO YA HA SIDO INGRESADO")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PATCH','DELETE'])
def detalle_pedido (request,id):
    try:
        pedido = Pedido.objects.get(id_pedido=id)
    except Pedido.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = PedidoSerializer(pedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#API TABLA STOCK
@api_view(['GET', 'POST'])
def lista_stocks(request):
    if request.method == 'GET':
        query = Stock.objects.all()
        serializer = StockSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StockSerializer(data = request.data)
        print("❤️ ", serializer)
        if serializer.is_valid():
            id = request.POST.get('id_stock', None)
            print(id)
            if id in Stock.objects.values_list('id_stock', flat=True):
                print("💙 ESTE PRODUCTO YA HA SIDO INGRESADO")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PATCH','DELETE'])
def detalle_stock (request,id):
    try:
        stock = Stock.objects.get(id_stock=id)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StockSerializer(stock)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = StockSerializer(stock, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#API TABLA PRECIOS
@api_view(['GET', 'POST'])
def lista_precios(request):
    if request.method == 'GET':
        query = Precio.objects.all()
        serializer = PrecioSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PrecioSerializer(data = request.data)
        print("❤️ ", serializer)
        if serializer.is_valid():
            id = request.POST.get('id_precio', None)
            print(id)
            if id in Precio.objects.values_list('id_precio', flat=True):
                print("💙 ESTE PRODUCTO YA HA SIDO INGRESADO")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PATCH','DELETE'])
def detalle_precio (request,id):
    try:
        precio = Precio.objects.get(id_precio=id)
    except Precio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PrecioSerializer(precio)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = PrecioSerializer(precio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        precio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

'''
#API TABLA OFERTA
@api_view(['GET', 'POST'])
def lista_ofertas(request):
    if request.method == 'GET':
        query = Oferta.objects.all()
        serializer = OfertaSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OfertaSerializer(data = request.data)
        print("❤️ ", serializer)
        if serializer.is_valid():
            id = request.POST.get('id_oferta', None)
            print(id)
            if id in Oferta.objects.values_list('id_oferta', flat=True):
                print("💙 ESTA OFERTA YA HA SIDO INGRESADA")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PATCH','DELETE'])
def detalle_oferta (request,id):
    try:
        oferta = Oferta.objects.get(id_oferta=id)
    except Oferta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OfertaSerializer(oferta)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = OfertaSerializer(oferta, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        oferta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

'''