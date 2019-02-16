from django.contrib import admin
from .models import Torneo

class TorneoAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Torneo,TorneoAdmin)
