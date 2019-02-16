from django import forms
from .models import Torneo, Participaciones

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['titulo','descripcion','participantes','fecha']

        labels = {
            'titulo': 'Titulo',
            'descripcion': 'Descripción',
            'participantes': 'Numero Participantes',
            'fecha': 'Fecha',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','style':'width:15cm'}),
            'participantes':  forms.NumberInput(attrs={'class':'form-control','style':'width:8cm'}),
            'fecha':  forms.DateTimeInput(attrs={'class':'form-control','style':'width:8cm', 'type':'Date'}),
        }

class ParticipacionesForm(forms.ModelForm):
    class Meta:
        model = Participaciones
        fields = ['puesto']

        labels = {
            'puesto': 'Puesto',
        }

        widgets = {
            'puesto':  forms.NumberInput(attrs={'class':'form-control','style':'width:4cm'}),
        }