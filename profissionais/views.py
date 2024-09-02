from django.shortcuts import render, get_object_or_404, redirect
from .models import Profissional


def lista_profissionais(request):
    profissionais = Profissional.objects.all()
    return render(
        request,
        "profissionais/lista_profissionais.html",
        {"profissionais": profissionais},
    )


def novo_profissional(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        especialidade = request.POST["especialidade"]
        telefone = request.POST["telefone"]
        profissional = Profissional(
            nome=nome, especialidade=especialidade, telefone=telefone
        )
        profissional.save()
        return redirect("lista_profissionais")
    return render(request, "profissionais/novo_profissional.html")


def editar_profissional(request, id):
    profissional = get_object_or_404(Profissional, id=id)
    if request.method == "POST":
        profissional.nome = request.POST["nome"]
        profissional.especialidade = request.POST["especialidade"]
        profissional.telefone = request.POST["telefone"]
        profissional.save()
        return redirect("lista_profissionais")
    return render(
        request,
        "profissionais/editar_profissional.html",
        {"profissional": profissional},
    )


def excluir_profissional(request, profissional_id):
    profissional = get_object_or_404(Profissional, id=profissional_id)
    profissional.delete()
    return redirect("lista_profissionais")
