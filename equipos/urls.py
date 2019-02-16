from django.urls import path
from . import views
from .views import  EquipoUpdate, EquipoDelete, JugadorPerfilUpdate

urlpatterns = [
    path('', views.equipos, name="equipos"),
    path('<int:id>/', views.infoequipo, name="equipo"),
    path('addEquipo/<int:id>/', views.EquipoCreate, name="equipo_add"),
    path('updateEquipo/<int:pk>/', EquipoUpdate.as_view(), name="equipo_edit"),
    path('deleteEquipo/<int:id>/', EquipoDelete, name="equipo_del"),
    path('perfil/', JugadorPerfilUpdate.as_view(), name='perfil' )

]