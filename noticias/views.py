from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from .models import Noticia
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import NoticiaForm

# Create your views here.

class NoticiasList(ListView):
    model = Noticia
    template_name = "noticias/noticias.html"

class NoticiaDetail(DetailView):
    model=Noticia
    template_name="noticias/noticia.html"

class NoticiaCreate(CreateView):
    model=Noticia
    form_class=NoticiaForm
    
    def get_success_url(self):
        return reverse_lazy('noticias') + '?add'

class NoticiaUpdate(UpdateView):
    model=Noticia
    form_class=NoticiaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('noticias') + '?edit'

class NoticiaDelete(DeleteView):
    model=Noticia
    
    def get_success_url(self):
        return reverse_lazy('noticias')+ '?del'
