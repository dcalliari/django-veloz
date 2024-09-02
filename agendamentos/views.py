from django.shortcuts import render, get_object_or_404, redirect
from .models import Agendamento
from pacientes.models import Paciente
from profissionais.models import Profissional


def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(
        request, "agendamentos/lista_agendamentos.html", {"agendamentos": agendamentos}
    )


def novo_agendamento(request):
    if request.method == "POST":
        paciente_id = request.POST["paciente"]
        profissional_id = request.POST["profissional"]
        data_hora = request.POST["data_hora"]
        observacoes = request.POST["observacoes"]

        paciente = Paciente.objects.get(id=paciente_id)
        profissional = Profissional.objects.get(id=profissional_id)
        agendamento = Agendamento(
            paciente=paciente,
            profissional=profissional,
            data_hora=data_hora,
            observacoes=observacoes,
        )
        agendamento.save()
        return redirect("lista_agendamentos")
    pacientes = Paciente.objects.all()
    profissionais = Profissional.objects.all()
    return render(
        request,
        "agendamentos/novo_agendamento.html",
        {"pacientes": pacientes, "profissionais": profissionais},
    )


def editar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    if request.method == "POST":
        agendamento.paciente_id = request.POST["paciente"]
        agendamento.profissional_id = request.POST["profissional"]
        agendamento.data_hora = request.POST["data_hora"]
        agendamento.observacoes = request.POST["observacoes"]
        agendamento.save()
        return redirect("lista_agendamentos")
    pacientes = Paciente.objects.all()
    profissionais = Profissional.objects.all()
    return render(
        request,
        "agendamentos/editar_agendamento.html",
        {
            "agendamento": agendamento,
            "pacientes": pacientes,
            "profissionais": profissionais,
        },
    )


def excluir_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    agendamento.delete()
    return redirect("lista_agendamentos")
