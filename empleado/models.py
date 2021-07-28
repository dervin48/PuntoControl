#-*- coding: utf-8 -*-
from django.db import models
from comun.models import *

class Empleado(Persona):
    dpi = models.CharField('DPI',max_length=14)
    class Meta():
        db_table = 'empledo'
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
# Create your models here.
class Telefono(models.Model):
    empleado= models.ForeignKey(
        Empleado, verbose_name='Empleado', on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(
        'numero de telefono', help_text='solo incluir numeros'
    )
    tipo = models.ForeignKey(
        TipoTelefono, verbose_name='Tipo Telefono',related_name='TelEmpleado', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s :  %s" %(self.empleado, self.numero)

    class Meta:
        verbose_name='Telefono de Empleado'
        verbose_name_plural = 'Telefono de Empleado'    