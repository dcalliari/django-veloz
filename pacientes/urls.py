from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_pacientes, name="lista_pacientes"),
    path("novo/", views.novo_paciente, name="novo_paciente"),
    path("<int:id>/editar/", views.editar_paciente, name="editar_paciente"),
    path("excluir/<int:paciente_id>/", views.excluir_paciente, name="excluir_paciente"),
]
