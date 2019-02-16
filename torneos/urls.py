from django.urls import path
from . import views
from .views import TorneoCreate, TorneoUpdate, TorneoDelete, NormasTemplate, addresultados


urlpatterns = [
    path('', views.torneos, name="torneos"),
    path('addTorneo', TorneoCreate.as_view(), name="torneo_add"),
    path('updateTorneo/<int:pk>/', TorneoUpdate.as_view(), name="torneo_edit"),
    path('deleteTorneo/<int:pk>/', TorneoDelete.as_view(), name="torneo_del"),
    path('normas', NormasTemplate.as_view(), name="normas"),
    path('torneo_apuntar/<int:id>/', views.torneo_apuntar, name="torneo_apuntar"),
    path('participaciones/<int:id>/', views.participaciones, name="participaciones"),
    path('addresultados/<int:pk>/', addresultados.as_view(), name="resultados"),
    path('addPuesto/<int:id>',views.addPuesto, name="addpuesto")
]