from django.db import models
from equipos.models import Equipo
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Torneo(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    descripcion = RichTextUploadingField(verbose_name="Descripcion")
    participantes = models.IntegerField(null=True, verbose_name="Participantes")
    fecha = models.DateField(null=True, blank=True, verbose_name="Fecha")
    equipos=models.ManyToManyField(Equipo,related_name="equipos", verbose_name="Equipos")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta():
        verbose_name="Torneo"
        verbose_name_plural="Torneos"
        ordering=["-created"]
    
    def __str__(self):
        return self.titulo

class Participaciones(models.Model):
    torneo= models.ForeignKey(Torneo, related_name="torneo", verbose_name="Torneo", on_delete=models.PROTECT, null=True, blank=True)
    equipo = models.ForeignKey(Equipo, related_name="equipo", verbose_name="Equipo", on_delete=models.PROTECT, null=True, blank=True)
    puesto=models.IntegerField(null=True, blank=True)