import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Marca(models.Model):
    nombre      = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre      = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre         = models.CharField(max_length=50)
    descripcion    = models.CharField(max_length=200, blank=True, null=True)
    preciounitario = models.DecimalField(default=0, decimal_places=3, max_digits=10, verbose_name='Precio Unitario')
    marca          = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True)
    categoria      = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    codigoexterno  = models.CharField(max_length=50, blank=True, verbose_name='Codigo Externo')
    stock          = models.IntegerField(default=0)
    imagen         = models.CharField(max_length=50, blank=True, null=False)
    enabled        = models.BooleanField(default=True, verbose_name='¿Producto En Venta?')
    ispromo        = models.BooleanField(default=False, verbose_name='¿En Promocion?')
    preciopromo    = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    unidadmedida   = models.IntegerField(default=1, verbose_name='Unidad de Medida')
    isfraccionado  = models.BooleanField(default=False, verbose_name='¿Es Fraccionado?')

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    nombre      = models.CharField(max_length=50,  blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    fecha      = models.DateTimeField('Fecha Creacion', auto_now=True)
    estado     = models.ForeignKey(Estado, on_delete=models.CASCADE)
    android_id = models.IntegerField(default=0, blank=True, null=True)
    subtotal   = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    monto      = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    montoabona = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    cliente    = models.ForeignKey(User, on_delete=models.CASCADE)
    localidad  = models.CharField(max_length=50, blank=True, null=True)
    calle      = models.CharField(max_length=50, blank=True, null=True)
    piso       = models.CharField(max_length=10, blank=True, null=True)
    nro        = models.CharField(max_length=10, blank=True, null=True)
    telefono   = models.CharField(max_length=25, blank=True, null=True)
    contacto   = models.CharField(max_length=50, blank=True, null=True)
    montodescuento    = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    cantidaddescuento = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    enviodomicilio    = models.BooleanField(default=False, verbose_name='¿Envio a Domicilio?')
    visto             = models.BooleanField(default=False)
    impreso           = models.BooleanField(default=False)
    tiempodemora      = models.CharField(max_length=10, default=False, verbose_name='Tiempo Demora')
    horarecepcion     = models.TimeField(verbose_name='Hora Recepcion', default= 0, blank=True, null=True)
    horaentrega       = models.TimeField(verbose_name='Hora Entrega', default=0)

    def __str__(self):
        return self.id


class Pedidodetalle(models.Model):
    cantidad = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    pedido   = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Parametro(models.Model):
    nombre       = models.CharField(max_length=50)
    descripcion  = models.CharField(max_length=100)
    valortexto   = models.CharField(max_length=100)
    valorinteger = models.IntegerField()
    valordecimal = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    valorfecha   = models.DateTimeField('Fecha')

    def __str__(self):
        return self.nombre



class Promo (models.Model):
    nombre           = models.CharField(max_length=50)
    descripcion      = models.CharField(max_length=100)
    enabled          = models.CharField(max_length=100)
    producto         = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad         = models.IntegerField()
    preciopromo      = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    importedescuento = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    precioanterior   = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    fechadesde       = models.DateTimeField('Fecha Desde')
    fechadesde       = models.DateTimeField('Fecha Hasta')

    def __str__(self):
        return self.nombre



class Dispenser(models.Model):
    nombre      = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    serie = models.CharField(max_length=200, blank=True, null=True)
    orden = models.IntegerField()

    def __str__(self):
        return self.nombre