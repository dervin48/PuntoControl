from django.contrib import admin
from .models import *


class DetalleVentaInLine(admin.TabularInline):
    model = DetalleVenta
    extra= 0
    autocomplete_fields = ['producto']

class VentaAdmin(admin.ModelAdmin):
    inlines=[DetalleVentaInLine]
    search_fields = ['cliente__nit','cliente__nombre', 'cliente__apellido']
    list_filter = ['fecha_venta', 'empresa', 'empleado']
    list_display= ['numero', 'fecha_venta', 'total', 
        'cliente' , 'empleado', 'empresa']
    readonly_fields = ['total']

admin.site.register(Venta, VentaAdmin)
# Register your models here.
