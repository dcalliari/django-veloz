from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_transacoes, name="lista_transacoes"),
    path("nova/", views.nova_transacao, name="nova_transacao"),
    path("<int:id>/editar/", views.editar_transacao, name="editar_transacao"),
    path(
        "excluir/<int:transacao_id>/", views.excluir_transacao, name="excluir_transacao"
    ),
]
