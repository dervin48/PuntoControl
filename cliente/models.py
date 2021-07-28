#-*- coding: utf-8 -*-
from django.db import models
from comun.models import *

class Cliente(Persona):
    nit = models.CharField('NIT',max_length=10)
    def __str__(self):
    	return '%s: %s, %s' %(self.nit, self.apellido, self.nombre)
    class Meta():
       db_table = 'cliente'
       verbose_name='Cliente'
       verbose_name_plural='Clientes'
       unique_together=['nombre', 'apellido']

class Telefono(models.Model):
    cliente= models.ForeignKey(
        Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(
        'numero de telefono', help_text='solo incluir numeros'
    )
    tipo = models.ForeignKey(
        TipoTelefono, verbose_name='Tipo Telefono',related_name='TelCliente', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s :  %s" %(self.cliente, self.numero)

    class Meta:
        verbose_name='Telefono de Cliente'
        verbose_name_plural = 'Telefono de Cliente'    
# Create your models here.
