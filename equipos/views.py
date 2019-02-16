from django.shortcuts import render, redirect, HttpResponse, get_list_or_404, get_object_or_404
from .models import Equipo, JugadorPerfil
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import EquipoForm, JugadorPerfilForm


# Create your views here.

def equipos(request):
    equipos = Equipo.objects.all()
    return render(request,"equipos/equipos.html", {'equipos':equipos})

def infoequipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    jugadores = JugadorPerfil.objects.filter(equipo=equipo)
    return render(request,"equipos/equipo.html", {'equipo':equipo}, {'jugadores':jugadores})

def EquipoCreate(request, id):
    equipo_form=EquipoForm()
    if request.method=="POST":
        equipo_form=EquipoForm(request.POST, request.FILES)
        print(request.POST)
        if equipo_form.is_valid():
            nombre=request.POST.get('nombre','')
            fundacion=request.POST.get('fundacion','')
            presidente=request.POST.get('presidente','')
            direccion=request.POST.get('direccion','')
            web=request.POST.get('web','')
            estadio=request.POST.get('estadio','')
            imagen=request.FILES.get('imagen','')
            equipo=Equipo(nombre=nombre, fundacion=fundacion, presidente=presidente, direccion=direccion, web=web, estadio=estadio, imagen=imagen)
            equipo.save()

            jugador=get_object_or_404(JugadorPerfil,id=id)
            jugador.equipo=equipo
            jugador.capitan=True
            jugador.save()
            return redirect(reverse('equipos') +'?add')
    return render(request,"equipos/equipo_form.html",{'form':equipo_form})

class EquipoUpdate(UpdateView):
    model=Equipo
    form_class=EquipoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('equipos') + '?edit'

def EquipoDelete(request, id):
    equipos = Equipo.objects.all()
    equipo=Equipo.objects.get(id=id)
    jugadores= JugadorPerfil.objects.filter(equipo=equipo.id)
    for jugador in jugadores:
        jugador.capitan=False
        jugador.save()
    equipo.delete()
    return redirect(reverse("equipos") + '?del')

class JugadorPerfilUpdate(UpdateView):
    model=JugadorPerfil
    template_name='equipos/perfil.html'
    form_class=JugadorPerfilForm

    def get_object(self):
        jugadorperfil, create = JugadorPerfil.objects.get_or_create(usuario=self.request.user)
        return jugadorperfil

    def get_success_url(self):
        return reverse_lazy('perfil') + '?act'
