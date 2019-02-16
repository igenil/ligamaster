from django.urls import path
from . import views
from .views import NoticiaCreate, NoticiaUpdate, NoticiaDelete, NoticiasList, NoticiaDetail


urlpatterns = [
    path('', NoticiasList.as_view(), name="noticias"),
    path('<int:pk>/', NoticiaDetail.as_view(), name="noticia"),
    path('addNoticia', NoticiaCreate.as_view(), name="noticia_add"),
    path('updateNoticia/<int:pk>/', NoticiaUpdate.as_view(), name="noticia_edit"),
    path('deleteNoticia/<int:pk>/', NoticiaDelete.as_view(), name="noticia_del"),
]