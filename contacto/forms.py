from django import forms

class FormularioContacto(forms.Form):
    mensaje = forms.CharField()
    mail = forms.EmailField()
