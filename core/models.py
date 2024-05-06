from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class TipoProducto(models.Model):
    TipoProducto = [
        (1, 'Herramientas Manuales'),#1- Herramientas Manuales
        (2, 'Materiales Basicos'),#2- Materiales Basicos
        (3, 'Equipo de Seguridad'), #3- Equipo de Seguridad
        (4, 'Tornillos y Anclajes'), #4-Tornillos y Anclajes
        (5, 'Fijaciones y Adhesivos'), #5-Fijaciones y Adhesivos
        (6, 'Equipos de Medicion'), #6-Equipos de Medicion
    ]
    id_tipo = models.IntegerField(choices=TipoProducto, primary_key=True)

    def __str__(self):
        for tipo_id, tipo_nombre in self.TipoProducto:
            if tipo_id == self.id_tipo:
                return tipo_nombre
        return str(self.id_tipo)

 #   def __str__(self):
    #    return str(self.tipo_nombre)


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, unique=True)
    precio = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999999)])
    stock = models.IntegerField()
    id_tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre