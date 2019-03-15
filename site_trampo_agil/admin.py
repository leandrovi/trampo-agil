from django.contrib import admin
from site_trampo_agil.models import Candidato, Empresa
from mural_vagas.models import Vaga

# Register your models here.
admin.site.register(Candidato)
admin.site.register(Empresa)
admin.site.register(Vaga)