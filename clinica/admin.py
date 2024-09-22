from django.contrib import admin
from clinica.models import Paciente, Profissional, Transacao, Agendamento

admin.site.register(Paciente)
admin.site.register(Profissional)
admin.site.register(Transacao)
admin.site.register(Agendamento)
