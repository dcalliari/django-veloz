from django.db import models
from pacientes.models import Paciente
from profissionais.models import Profissional


class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente} - {self.data_hora}"
