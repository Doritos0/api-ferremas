from django.db import models
from django.core.exceptions import ValidationError

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
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, unique=True)
    id_tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Producto {self.nombre}"


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
    fec_ter = models.DateField(blank=True, null=True, editable=False)
    precio = models.IntegerField()

    def __str__(self):
        return f"Precio {self.fec_ini} termino {self.fec_ter}"
    
    def clean(self):
        # Verificamos si la fecha de inicio es mayor que la fecha de inicio de la entrada anterior
        if self.fec_ini:
            entradas_anteriores = Precio.objects.filter(
                id_producto=self.id_producto,
                fec_ini__lt=self.fec_ini
            ).order_by('-fec_ini')

            if entradas_anteriores.exists():
                ultima_entrada_anterior = entradas_anteriores.first()
                print("💚 ESTA FECHA ",self.fec_ini," NO DEBERIA SER MAYOR A ",ultima_entrada_anterior.fec_ter," ID ",ultima_entrada_anterior.id_precio)
                if ultima_entrada_anterior.fec_ter == self.fec_ini:
                    raise ValidationError("Ya hay un precio para esta fecha")
                elif ultima_entrada_anterior.fec_ter is None or self.fec_ini >= ultima_entrada_anterior.fec_ter:
                    print("💙 FUNCIONA")
                else:
                    raise ValidationError("La fecha de inicio debe ser posterior a la última entrada")

    def save(self, *args, **kwargs):
        if self.fec_ini:
            entradas_anteriores = Precio.objects.filter(
                id_producto=self.id_producto,
                fec_ini__lt=self.fec_ini
            ).order_by('-fec_ini')

            if entradas_anteriores.exists():
                ultima_entrada_anterior = entradas_anteriores.first()
                ultima_entrada_anterior.fec_ter = self.fec_ini
                ultima_entrada_anterior.save()

        super(Precio, self).save(*args, **kwargs)
        
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
    

