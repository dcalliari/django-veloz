from django.urls import path
from .views import (
    Home,
    CadastrarPacientes,
    CadastrarProfissionais,
    CadastrarTransacoes,
    CadastrarAgendamentos,
    ListarPacientes,
    ListarProfissionais,
    ListarTransacoes,
    ListarAgendamentos,
    EditarPaciente,
    EditarProfissional,
    EditarTransacao,
    EditarAgendamento,
    delete,
)

app_name = "clinica"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path(
        "cadastrar-pacientes/", CadastrarPacientes.as_view(), name="cadastrar_pacientes"
    ),
    path(
        "cadastrar-profissionais/",
        CadastrarProfissionais.as_view(),
        name="cadastrar_profissionais",
    ),
    path(
        "cadastrar-transacoes/",
        CadastrarTransacoes.as_view(),
        name="cadastrar_transacoes",
    ),
    path(
        "cadastrar-agendamentos/",
        CadastrarAgendamentos.as_view(),
        name="cadastrar_agendamentos",
    ),
    path("listar-pacientes/", ListarPacientes.as_view(), name="listar_pacientes"),
    path(
        "listar-profissionais/",
        ListarProfissionais.as_view(),
        name="listar_profissionais",
    ),
    path("listar-transacoes/", ListarTransacoes.as_view(), name="listar_transacoes"),
    path(
        "listar-agendamentos/", ListarAgendamentos.as_view(), name="listar_agendamentos"
    ),
    path("editar/<int:pk>", EditarPaciente.as_view(), name="editar_paciente"),
    path(
        "editar-profissional/<int:pk>",
        EditarProfissional.as_view(),
        name="editar_profissional",
    ),
    path(
        "editar-transacao/<int:pk>", EditarTransacao.as_view(), name="editar_transacao"
    ),
    path(
        "editar-agendamento/<int:pk>",
        EditarAgendamento.as_view(),
        name="editar_agendamento",
    ),
    path("excluir/<str:model_name>/<int:pk>", delete, name="excluir"),
]
