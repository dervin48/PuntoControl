from django.contrib import admin
from .models import *


class TelefonoInLine(admin.TabularInline):
    model=Telefono
    extra = 0
    #autocomplete_fields = ['tipo']
    raw_id_fields = ['tipo']

class ClienteAdmin(admin.ModelAdmin):
    inlines = [TelefonoInLine]
    search_fields = ['nombre', 'apellido']  # busquedas
    list_filter = ['fecha_nacimiento']  # filtros dinamicos
    list_display = ['nit','nombre', 'apellido','edad', 'fecha_nacimiento' ,'correo']


    
#admin.site.register(Telefono)


    
admin.site.register(Cliente, ClienteAdmin)


# Register your models here.
