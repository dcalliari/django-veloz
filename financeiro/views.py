from django.shortcuts import render, get_object_or_404, redirect
from .models import Transacao


def lista_transacoes(request):
    transacoes = Transacao.objects.all()
    return render(
        request, "financeiro/lista_transacoes.html", {"transacoes": transacoes}
    )


def nova_transacao(request):
    if request.method == "POST":
        descricao = request.POST["descricao"]
        valor = request.POST["valor"]
        data = request.POST["data"]
        transacao = Transacao(descricao=descricao, valor=valor, data=data)
        transacao.save()
        return redirect("lista_transacoes")
    return render(request, "financeiro/nova_transacao.html")


def editar_transacao(request, id):
    transacao = get_object_or_404(Transacao, id=id)
    if request.method == "POST":
        transacao.descricao = request.POST["descricao"]
        transacao.valor = request.POST["valor"]
        transacao.data = request.POST["data"]
        transacao.save()
        return redirect("lista_transacoes")
    return render(request, "financeiro/editar_transacao.html", {"transacao": transacao})


def excluir_transacao(request, transacao_id):
    transacao = get_object_or_404(Transacao, id=transacao_id)
    transacao.delete()
    return redirect("lista_transacoes")
