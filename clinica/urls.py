from django.contrib import admin
from django.urls import include, path
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("pacientes/", include("pacientes.urls")),
    path("profissionais/", include("profissionais.urls")),
    path("agendamentos/", include("agendamentos.urls")),
    path("financeiro/", include("financeiro.urls")),
]
