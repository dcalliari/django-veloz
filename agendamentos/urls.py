from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_agendamentos, name="lista_agendamentos"),
    path("novo/", views.novo_agendamento, name="novo_agendamento"),
    path("<int:id>/editar/", views.editar_agendamento, name="editar_agendamento"),
    path(
        "excluir/<int:agendamento_id>/",
        views.excluir_agendamento,
        name="excluir_agendamento",
    ),
]
