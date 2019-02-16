from django import forms
from .models import Equipo, JugadorPerfil
from captcha.fields import ReCaptchaField

class EquipoForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Equipo
        fields = ['nombre','fundacion','presidente','direccion','web','estadio','imagen']

        labels = {
            'nombre': 'Nombre',
            'fundacion': 'Fundación',
            'presidente': 'Presidente',
            'direccion': 'Dirección',
            'web': 'Página Web',
            'estadio': 'Estadio',
            'imagen': 'Imagen',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
            'fundacion': forms.NumberInput(attrs={'class':'form-control','style':'width:8cm'}),
            'presidente':  forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
            'web': forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
            'estadio': forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
        }

class JugadorPerfilForm(forms.ModelForm):
        class Meta:
            model = JugadorPerfil
            fields = ['nombre','imagen','edad','equipo','goles','pais','posicion','altura']

            labels = {
                'nombre': 'Nombre',
                'imagen': 'Foto',
                'edad': 'Edad',
                'equipo': 'Equipo',
                'goles': 'Goles',
                'pais': 'País',
                'posicion': 'Posicion',
                'altura': 'Altura',
            }

            widgets = {
                'nombre': forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
                'edad':  forms.NumberInput(attrs={'class':'form-control','style':'width:8cm'}),
                'equipo': forms.Select(attrs={'class':'form-control','style':'width:8cm'}),
                'goles': forms.NumberInput(attrs={'class':'form-control','style':'width:8cm'}),
                'pais': forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
                'posicion': forms.TextInput(attrs={'class':'form-control','style':'width:8cm'}),
                'altura': forms.NumberInput(attrs={'class':'form-control','style':'width:8cm'}),
            }