from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.urls import reverse_lazy
from .forms import TorneoForm, ParticipacionesForm
from .models import Torneo, Participaciones

# Create your views here.

def torneos(request):
    torneos = Torneo.objects.all()
    return render(request,"torneos/torneos.html", {'torneos':torneos})

class TorneoCreate(CreateView):
    model=Torneo
    form_class=TorneoForm
    
    def get_success_url(self):
        return reverse_lazy('torneos') + '?add'

class TorneoUpdate(UpdateView):
    model=Torneo
    form_class=TorneoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('torneos') + '?edit'

class TorneoDelete(DeleteView):
    model=Torneo
    def get_success_url(self):
        return reverse_lazy('torneos')+ '?del'

def participaciones(request, id):
    participaciones=Participaciones.objects.filter(torneo=id)
    form=ParticipacionesForm
    return render(request,"torneos/participaciones.html",{"participaciones":participaciones,"form":form})

def addPuesto(request, id):
    participacion = Participaciones.objects.get(id=id)
    participacion.puesto=request.POST.get('puesto','')
    participacion.save()
    participaciones=Participaciones.objects.filter(torneo=participacion.torneo)
    form=ParticipacionesForm
    return render(request,"torneos/participaciones.html",{"participaciones":participaciones,"form":form})


class addresultados(UpdateView):
    model=Participaciones
    form_class=ParticipacionesForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('torneos') + '?resul'

class NormasTemplate(TemplateView):
    template_name='torneos/normas.html'

def torneo_apuntar(request,id):
    torneo = get_object_or_404(Torneo,id=id)
    equipo_user=request.user.perfil.equipo
    torneos = Torneo.objects.all()
    if (equipo_user==None):
        error="Lo sentimos,no formas parte de ningun equipo aun"
        return render(request,'torneos/torneos.html',{'error':error,'torneos':torneos})
    if (Participaciones.objects.filter(equipo=equipo_user, torneo=torneo)):
        error1="Tu equipo ya esta apuntado a este torneo"
        return render(request,'torneos/torneos.html',{'error1':error1,'torneos':torneos})
    else:
        if (torneo.participantes>0 and request.user.perfil.capitan==True):
            participacion=Participaciones(torneo=torneo, equipo=equipo_user)
            participacion.save()
            torneo.participantes-=1
            torneo.save()
            success="Tu equipo ha sido apuntado correctamente"
            return render(request,'torneos/torneos.html',{'success':success,'torneos':torneos})
            
        else:
            error2="Lo sentimos, el torneo ha llegado al maximo de participantes"
    return render(request,'torneos/torneos.html',{'error2':error2,'torneos':torneos})


