from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import FormularioContacto

# Create your views here.

def contactomail(request):
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            msg=True
            asunto = 'Mensaje desde Django'
            mensaje = formulario.cleaned_data['mensaje']
            mail = EmailMessage(asunto, mensaje, to=['ignaciogenil@gmail.com'])
            mail.send()
        return render(request,'contacto/contacto_mail.html', {'msg':msg})
    else:
        formulario = FormularioContacto()
    
    return render(request,'contacto/contacto_mail.html', {'formulario':formulario})