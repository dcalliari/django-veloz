from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from agendamentos.views import AgendamentoViewSet
from financeiro.views import TransacaoViewSet
from pacientes.views import PacienteViewSet
from profissionais.views import ProfissionalViewSet

router = DefaultRouter()
router.register(r"profissionais", ProfissionalViewSet)
router.register(r"agendamentos", AgendamentoViewSet)
router.register(r"transacoes", TransacaoViewSet)
router.register(r"pacientes", PacienteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
