from django.db import models


class Empresa(models.Model):
    empresa=models.CharField('empresa', max_length=50)

    def __str__(self):
        return self.empresa

    class Meta: 
        db_table ='empresa'
        verbose_name ='empresa'
        verbose_name_plural = 'empresas' 

# Create your models here.
