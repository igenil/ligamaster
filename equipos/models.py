from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
    nombre= models.CharField(max_length=100, verbose_name="Nombre")
    fundacion= models.IntegerField(verbose_name="Fundación")
    presidente= models.CharField(max_length=100, verbose_name="Presidente")
    direccion= models.CharField(max_length=100, verbose_name="Dirección")
    web = models.CharField(max_length=100, verbose_name="Página Web")
    estadio= models.CharField(max_length=100, verbose_name="Estadio")
    imagen= models.ImageField(upload_to="equipos", verbose_name="Logotipo")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name="Equipo"
        verbose_name_plural="Equipos"
        ordering=["nombre"]
    
    def __str__(self):
        return self.nombre
    
class JugadorPerfil (models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=True, blank=True)
    imagen = models.ImageField(upload_to="equipos", verbose_name="Foto", null=True, blank=True)
    edad = models.IntegerField(verbose_name="Edad", null=True, blank=True)
    equipo = models.ForeignKey(Equipo, related_name="jugadores", verbose_name="Equipo", on_delete=models.SET_NULL, null=True, blank=True)
    goles = models.IntegerField(verbose_name="Goles",null=True, blank=True)
    pais = models.CharField(max_length=100, verbose_name="País",null=True, blank=True)
    posicion = models.CharField(max_length=100, verbose_name="Posición", null=True, blank=True)
    altura = models.IntegerField(verbose_name="Estatura", null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    capitan = models.BooleanField(verbose_name="Capitan", default=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta():
        verbose_name="Jugador"
        verbose_name_plural="Jugadores"
        ordering=["-goles"]
    
    def __str__(self):
        return self.usuario.username
