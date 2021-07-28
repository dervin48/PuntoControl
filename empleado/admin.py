from django.contrib import admin
from .models import *
# Register your models here.

class TelefonoInLine(admin.TabularInline):
    model=Telefono
    extra = 0
    autocomplete_fields = ['tipo']
    #raw_id_fields = ['tipo']
class EmpleadoAdmin(admin.ModelAdmin):
    inlines = [TelefonoInLine]
    search_fields = ['nombre', 'apellido']  # busquedas
    list_filter = ['fecha_nacimiento']  # filtros dinamicos
    list_display = ['dpi','nombre', 'apellido', 'edad', 'fecha_nacimiento' ,'correo']

    
admin.site.register(Empleado, EmpleadoAdmin)
#admin.site.register(Telefono)
