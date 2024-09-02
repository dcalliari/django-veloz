from django.db import models


class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
