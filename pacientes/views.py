from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente


def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/lista_pacientes.html", {"pacientes": pacientes})


def novo_paciente(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        data_nascimento = request.POST["data_nascimento"]
        endereco = request.POST["endereco"]
        telefone = request.POST["telefone"]
        paciente = Paciente(
            nome=nome,
            data_nascimento=data_nascimento,
            endereco=endereco,
            telefone=telefone,
        )
        paciente.save()
        return redirect("lista_pacientes")
    return render(request, "pacientes/novo_paciente.html")


def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == "POST":
        paciente.nome = request.POST["nome"]
        paciente.data_nascimento = request.POST["data_nascimento"]
        paciente.endereco = request.POST["endereco"]
        paciente.telefone = request.POST["telefone"]
        paciente.save()
        return redirect("lista_pacientes")
    return render(request, "pacientes/editar_paciente.html", {"paciente": paciente})


def excluir_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    paciente.delete()
    return redirect("lista_pacientes")
