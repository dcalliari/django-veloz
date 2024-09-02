from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_profissionais, name="lista_profissionais"),
    path("novo/", views.novo_profissional, name="novo_profissional"),
    path("<int:id>/editar/", views.editar_profissional, name="editar_profissional"),
    path(
        "excluir/<int:profissional_id>/",
        views.excluir_profissional,
        name="excluir_profissional",
    ),
]
