# Generated by Django 4.2.6 on 2024-05-15 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cliente', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('fono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo', models.CharField(choices=[('Herramientas Manuales', 'Herramientas Manuales'), ('Materiales Basicos', 'Materiales Basicos'), ('Equipo de Seguridad', 'Equipo de Seguridad'), ('Tornillos y Anclajes', 'Tornillos y Anclajes'), ('Fijaciones y Adhesivos', 'Fijaciones y Adhesivos'), ('Equipos de Medicion', 'Equipos de Medicion')], max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id_stock', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('id_producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='id_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoproducto'),
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id_precio', models.AutoField(primary_key=True, serialize=False)),
                ('fec_ini', models.DateField()),
                ('fec_ter', models.DateField()),
                ('precio', models.IntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateField(auto_now_add=True)),
                ('estado_pedido', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En proceso', 'En proceso'), ('Completado', 'Completado')], max_length=10)),
                ('total', models.IntegerField()),
                ('rut_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
    ]
