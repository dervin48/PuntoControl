from django.db import models
from cliente.models import Cliente
from empleado.models import Empleado
from empresa.models import Empresa
from producto.models import Producto
from .models import *

class Venta(models.Model):
    empresa=models.ForeignKey(
        Empresa, verbose_name='Empresa',on_delete=models.CASCADE)
    cliente=models.ForeignKey(
        Cliente, verbose_name='Cliente',on_delete=models.CASCADE)
    empleado= models.ForeignKey(
        Empleado, verbose_name='Empleado', on_delete=models.CASCADE)
    fecha_venta= models.DateField('fecha venta')
    numero =  models.IntegerField('numero')
    total = models.DecimalField ('total', max_digits=10,
        decimal_places=2, editable=False, default=0.00)

    def __str__(self):
        return "%s (%s)" % (self.numero, self.fecha_venta)

    class Meta: 
        db_table='venta'
        verbose_name='venta'
        verbose_name_plural='ventas'
        
class DetalleVenta(models.Model):
    venta =models.ForeignKey(
        Venta, verbose_name='venta',on_delete=models.CASCADE)
    producto = models.ForeignKey(
        Producto, verbose_name='producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad')
    sub_total = models.DecimalField('sub_total', max_digits=10,
        decimal_places=2, default=0.00)

    def __str__(self):
        return "%s (%s)" % (self.venta, self.producto)

    class Meta:
        db_table ='ventas_detalle'
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'




    

# Create your models here.
