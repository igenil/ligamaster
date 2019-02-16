from django.contrib import admin
from .models import Equipo, JugadorPerfil
# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class JugadorPerfilAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Equipo,EquipoAdmin)
admin.site.register(JugadorPerfil,JugadorPerfilAdmin)
