from django.contrib import admin
from .models import *

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'marca__marca']
    list_filter = ['marca']
    list_display = ['nombre', 'marca', 'fecha_expiracion', 'precio', 'existencia']

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)

# Register your models here.
