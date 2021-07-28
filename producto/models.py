from django.db import models


class Marca(models.Model):
    marca=models.CharField('marca', max_length=50)

    def __str__(self):
        return self.marca

    class Meta: 
        verbose_name ='marca'
        verbose_name_plural ='marcas' 

class Producto(models.Model):
    nombre=models.CharField('nombre ', max_length=50)
    marca= models.ForeignKey(
        Marca, verbose_name='Marca', on_delete=models.CASCADE,
        null= True, blank=True)
    fecha_expiracion = models.DateField('fecha expiracion', null = True, blank=True)
    precio = models.DecimalField('precio' ,max_digits=8, decimal_places=2)
    existencia = models.IntegerField('existencia')


    def __str__(self):
        return "%s :  %s" %(self.nombre, self.marca)

    class Meta:
        db_table='producto'
        verbose_name='Producto'
        verbose_name_plural = 'Productos'    