from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from clinica.forms import PacienteForm, ProfissionalForm, TransacaoForm, AgendamentoForm
from clinica.models import Paciente, Profissional, Transacao, Agendamento


class Home(TemplateView):
    template_name = "index.html"


class ListarPacientes(ListView):
    template_name = "listar_pacientes.html"
    model = Paciente
    context_object_name = "pacientes"


class ListarProfissionais(ListView):
    template_name = "listar_profissionais.html"
    model = Profissional
    context_object_name = "profissionais"


class ListarTransacoes(ListView):
    template_name = "listar_transacoes.html"
    model = Transacao
    context_object_name = "transacoes"


class ListarAgendamentos(ListView):
    template_name = "listar_agendamentos.html"
    model = Agendamento
    context_object_name = "agendamentos"


class CadastrarPacientes(CreateView):
    template_name = "cadastrar_pacientes.html"
    model = Paciente
    form_class = PacienteForm
    success_url = "/"

    def form_valid(self, form):
        paciente = form.save(commit=True)
        return super().form_valid(form)


class CadastrarProfissionais(CreateView):
    template_name = "cadastrar_profissionais.html"
    model = Profissional
    form_class = ProfissionalForm
    success_url = "/"

    def form_valid(self, form):
        profissional = form.save(commit=True)
        return super().form_valid(form)


class CadastrarTransacoes(CreateView):
    template_name = "cadastrar_transacoes.html"
    model = Transacao
    form_class = TransacaoForm
    success_url = "/"

    def form_valid(self, form):
        transacao = form.save(commit=True)
        return super().form_valid(form)


class CadastrarAgendamentos(CreateView):
    template_name = "cadastrar_agendamentos.html"
    model = Agendamento
    form_class = AgendamentoForm
    success_url = "/"

    def form_valid(self, form):
        agendamento = form.save(commit=True)
        return super().form_valid(form)


class EditarPaciente(UpdateView):
    template_name = "editar.html"
    model = Paciente
    form_class = PacienteForm
    success_url = "/listar-pacientes"

    def form_valid(self, form):
        paciente = form.save(commit=True)
        return super().form_valid(form)


class EditarProfissional(UpdateView):
    template_name = "editar.html"
    model = Profissional
    form_class = ProfissionalForm
    success_url = "/listar-profissionais"

    def form_valid(self, form):
        profissional = form.save(commit=True)
        return super().form_valid(form)


class EditarTransacao(UpdateView):
    template_name = "editar.html"
    model = Transacao
    form_class = TransacaoForm
    success_url = "/listar-transacoes"

    def form_valid(self, form):
        transacao = form.save(commit=True)
        return super().form_valid(form)


class EditarAgendamento(UpdateView):
    template_name = "editar.html"
    model = Agendamento
    form_class = AgendamentoForm
    success_url = "/listar-agendamentos"

    def form_valid(self, form):
        agendamento = form.save(commit=True)
        return super().form_valid(form)


def delete(request, model_name, pk):
    model_map = {
        "paciente": Paciente,
        "profissional": Profissional,
        "transacao": Transacao,
        "agendamento": Agendamento,
    }

    model = model_map.get(model_name)
    if not model:
        raise Http404("Model not found")

    instance = model.objects.get(pk=pk)
    instance.delete()

    redirect_map = {
        "paciente": "clinica:listar_pacientes",
        "profissional": "clinica:listar_profissionais",
        "transacao": "clinica:listar_transacoes",
        "agendamento": "clinica:listar_agendamentos",
    }

    return redirect(redirect_map.get(model_name, "/"))
