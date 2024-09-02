from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
