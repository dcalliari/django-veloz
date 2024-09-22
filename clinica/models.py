from django.db import models


# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(
        max_length=1, choices=[("M", "Masculino"), ("F", "Feminino")]
    )
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    registro_profissional = models.CharField(max_length=50, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"


class Transacao(models.Model):
    TIPO_TRANSACAO = [
        ("C", "Crédito"),
        ("D", "Débito"),
    ]

    paciente = models.ForeignKey(
        Paciente, on_delete=models.SET_NULL, null=True, blank=True
    )
    profissional = models.ForeignKey(
        Profissional, on_delete=models.SET_NULL, null=True, blank=True
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=TIPO_TRANSACAO)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.valor} - {self.data.strftime('%d/%m/%Y')}"


class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_horario = models.DateTimeField()
    descricao = models.TextField(null=True, blank=True)
    confirmado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Agendamento - {self.paciente.nome} com {self.profissional.nome} em {self.data_horario.strftime('%d/%m/%Y %H:%M')}"
