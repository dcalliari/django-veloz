from rest_framework import viewsets
from .models import Transacao
from .serializers import TransacaoSerializer


class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
