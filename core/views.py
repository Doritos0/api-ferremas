import json
from django.http import JsonResponse
from django.shortcuts import redirect, render

# CREACION DE API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

#IMPORTAMOS EL MODELO
from .models import Productos, TipoProducto
from .serializers import ProductoSerializer, TipoProductoSerializer

# Create your views here.


#TABLA PRODUCTOS API
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_productos (request):
    if request.method == 'GET':
        query = Productos.objects.all()
        serializer = ProductoSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data = request.data)
        print("❤️ ", serializer)
        if serializer.is_valid():
            id = request.POST.get('id_producto', None)
            print(id)
            if id in Productos.objects.values_list('id_producto', flat=True):
                print("💙 ESTE PRODUCTO YA HA SIDO INGRESADO")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_producto (request,id):
    try:
        producto = Productos.objects.get(id_producto=id)
    except Productos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ProductoSerializer(producto,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method =='DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


#API TABLA TIPO_PRODUCTO
@api_view(['GET', 'POST'])
def lista_tipo (request):
    if request.method == 'GET':
        query = TipoProducto.objects.all()
        serializer = TipoProductoSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TipoProductoSerializer(data = request.data)
        print("❤️ ", serializer)
        if serializer.is_valid():
            id = request.POST.get('id_producto', None)
            print(id)
            if id in TipoProducto.objects.values_list('id_tipo', flat=True):
                print("💙 ESTE PRODUCTO YA HA SIDO INGRESADO")
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_tipo (request,id):
    try:
        tipo = TipoProducto.objects.get(id_tipo=id)
    except TipoProducto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TipoProductoSerializer(tipo)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = TipoProductoSerializer(tipo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method =='DELETE':
        tipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 