# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GestionBoleta(models.Model):
    direccion_venta = models.CharField(max_length=50, blank=True, null=True)
    fecha_emision = models.DateTimeField()
    numero_boleta = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'gestion_boleta'


class GestionCliente(models.Model):
    persona_ptr = models.OneToOneField('GestionPersona', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'gestion_cliente'


class GestionDetalleBoleta(models.Model):
    boleta_ptr = models.OneToOneField(GestionBoleta, models.DO_NOTHING, primary_key=True)
    producto_ptr = models.OneToOneField('GestionProducto', models.DO_NOTHING)
    cantidad = models.IntegerField()
    monto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gestion_detalle_boleta'


class GestionDetalleFactura(models.Model):
    factura_ptr = models.OneToOneField('GestionFactura', models.DO_NOTHING, primary_key=True)
    nombre_producto = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestion_detalle_factura'


class GestionEmpleado(models.Model):
    persona_ptr = models.OneToOneField('GestionPersona', models.DO_NOTHING, primary_key=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    correo_electronico = models.CharField(max_length=254, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestion_empleado'


class GestionFactura(models.Model):
    sitio_compra = models.CharField(max_length=50, blank=True, null=True)
    fecha_emision = models.DateTimeField()
    nro_factura = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'gestion_factura'


class GestionPersona(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=50, blank=True, null=True)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestion_persona'


class GestionProducto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    stock = models.IntegerField()
    marca = models.CharField(max_length=50, blank=True, null=True)
    unidad_medida = models.IntegerField()
    codigo_barra = models.IntegerField()
    precio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gestion_producto'


class Password(models.Model):
    id = models.FloatField(primary_key=True)
    password_hash = models.TextField()  # This field type is a guess.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')

    class Meta:
        managed = False
        db_table = 'password'


class ProductosBoleta(models.Model):
    direccion_venta = models.CharField(max_length=50, blank=True, null=True)
    fecha_emision = models.DateTimeField()
    numero_boleta = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'productos_boleta'


class ProductosCliente(models.Model):
    persona_ptr = models.OneToOneField('ProductosPersona', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'productos_cliente'


class ProductosDetalleFactura(models.Model):
    factura_ptr = models.OneToOneField('ProductosFactura', models.DO_NOTHING, primary_key=True)
    nombre_producto = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_detalle_factura'


class ProductosEmpleado(models.Model):
    persona_ptr = models.OneToOneField('ProductosPersona', models.DO_NOTHING, primary_key=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    correo_electronico = models.CharField(max_length=254, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_empleado'


class ProductosFactura(models.Model):
    sitio_compra = models.CharField(max_length=50, blank=True, null=True)
    fecha_emision = models.DateTimeField()
    nro_factura = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'productos_factura'


class ProductosPersona(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=50, blank=True, null=True)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_persona'


class ProductosProducto(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    stock = models.IntegerField()
    marca = models.CharField(max_length=50, blank=True, null=True)
    unidad_medida = models.IntegerField()
    codigo_barra = models.IntegerField()
    precio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'productos_producto'


class Role(models.Model):
    id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'role'


class User(models.Model):
    id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    father_surname = models.CharField(max_length=50, blank=True, null=True)
    mother_surname = models.CharField(max_length=50, blank=True, null=True)
    rut = models.FloatField(blank=True, null=True)
    roleid = models.ForeignKey(Role, models.DO_NOTHING, db_column='roleid')
    email = models.CharField(max_length=100, blank=True, null=True)
    sueldo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
