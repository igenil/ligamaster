from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo','descripcion','contenido','imagen']

        labels = {
            'titulo': 'Titulo',
            'descripcion': 'Descripcion',
            'contenido': 'Contenido',
            'imagen': 'Imagen',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
            'contenido':  forms.Textarea(attrs={'class':'form-control','style':'width:15cm'}),
        }
