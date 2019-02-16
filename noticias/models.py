from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
    contenido=RichTextUploadingField()
    imagen=models.ImageField(upload_to="noticias")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name="Noticia"
        verbose_name_plural="Noticias"
        ordering=["-created"]
    
    def __str__(self):
        return self.titulo
