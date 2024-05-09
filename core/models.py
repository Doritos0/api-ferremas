from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, unique=True)
    precio = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999999)])
    stock = models.IntegerField()
    id_tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Producto {self.nombre}"


class Cliente(models.Model):
    rut_cliente = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)
    fono = models.IntegerField()

    def __str__(self):
        return f"Cliente {self.nombre}"
    

class Pedido(models.Model):
    Estado = [
        ('Pendiente','Pendiente'),
        ('En proceso','En proceso'),
        ('Completado','Completado'),
    ]
    id_pedido = models.AutoField(primary_key=True)
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add=True)
    estado_pedido = models.CharField(choices=Estado, max_length=10)
    total = models.IntegerField()

    def __str__(self):
        return f"Pedido {self.fecha_pedido}"