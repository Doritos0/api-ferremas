from django.db import models
from django.core.exceptions import ValidationError
import json

# Create your models here.
class TipoProducto(models.Model):
    TipoProducto = [
        ('Herramientas Manuales','Herramientas Manuales'),#1- Herramientas Manuales
        ('Materiales Basicos', 'Materiales Basicos'),#2- Materiales Basicos
        ('Equipo de Seguridad', 'Equipo de Seguridad'), #3- Equipo de Seguridad
        ('Tornillos y Anclajes', 'Tornillos y Anclajes'), #4-Tornillos y Anclajes
        ('Fijaciones y Adhesivos', 'Fijaciones y Adhesivos'), #5-Fijaciones y Adhesivos
        ('Equipos de Medicion', 'Equipos de Medicion'), #6-Equipos de Medicion
    ]
    id_tipo = models.CharField(choices=TipoProducto, primary_key=True, max_length=50)

    def __str__(self):
        return self.id_tipo

 #   def __str__(self):
    #    return str(self.tipo_nombre)


class Producto(models.Model):
    Oferta = [
        (1, 'Si'),
        (0, 'No'),
    ]
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, unique=True)
    oferta = models.IntegerField(choices=Oferta)
    porcentaje = models.IntegerField(null=True, blank=True)
    id_tipo = models.ForeignKey('TipoProducto', on_delete=models.CASCADE)

    def __str__(self):
        return f"Producto {self.nombre}"

    def save(self, *args, **kwargs):
        if self.porcentaje is not None and (self.porcentaje < 0 or self.porcentaje > 100):
            raise ValueError("El porcentaje debe estar entre 0 y 100.")
        super().save(*args, **kwargs)


class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    id_producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Stock de Producto: {self.id_producto.nombre}"

class Precio(models.Model):
    id_precio = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fec_ini = models.DateField()
    fec_ter = models.DateField()
    precio = models.IntegerField()

    def __str__(self):
        return f"Precio {self.fec_ini} termino {self.fec_ter}"

class Usuario(models.Model):
    Tipo_usuario = [
        (0, 'Cliente'),
        (1, 'Administrador')
    ]
    id_usuario = models.AutoField(primary_key=True)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=64)
    tipo = models.IntegerField(choices = Tipo_usuario)
    
    def __str__(self):
        return f"Usuario: {self.user}"

class Pedido(models.Model):
    Estado = [
        ('Pendiente','Pendiente'),
        ('En proceso','En proceso'),
        ('Completado','Completado'),
    ]
    Tipo_Pedido = [
        (0,'Retiro en Tienda'),
        (1,'Envio'),
    ]
    id_pedido = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length = 100)
    correo = models.CharField(max_length=100)
    detalle_pedido = models.CharField(max_length=1000, editable=False)
    fecha_pedido = models.DateField(auto_now_add=True)
    tipo_pedido = models.IntegerField(choices = Tipo_Pedido)
    estado_pedido = models.CharField(choices=Estado, max_length=10)
    total = models.IntegerField()

    def __str__(self):
        return f"Pedido {self.fecha_pedido}"
    
'''
class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    porcentaje = models.IntegerField()

    def __str__(self):
        return f"{self.id_producto.nombre} con {self.porcentaje}% de oferta"
'''
