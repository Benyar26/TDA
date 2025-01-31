# Generated by Django 4.2.7 on 2023-11-13 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('direccion_venta', models.CharField(default='', max_length=50)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('numero_boleta', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('sitio_compra', models.CharField(max_length=50)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('nro_factura', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('stock', models.IntegerField(default=0)),
                ('marca', models.CharField(max_length=50)),
                ('unidad_medida', models.IntegerField(default=0)),
                ('codigo_barra', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_boleta',
            fields=[
                ('producto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='gestion.producto')),
                ('boleta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion.boleta')),
                ('cantidad', models.IntegerField(default=0)),
                ('monto', models.IntegerField(default=0)),
            ],
            bases=('gestion.boleta', 'gestion.producto'),
        ),
        migrations.CreateModel(
            name='Detalle_factura',
            fields=[
                ('factura_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion.factura')),
                ('nombre_producto', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('proveedor', models.CharField(max_length=50)),
            ],
            bases=('gestion.factura',),
        ),
    ]
