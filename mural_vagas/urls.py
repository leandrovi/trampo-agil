from django.contrib import admin
from django.urls import path
from mural_vagas.views import render_mural, render_candidaturas, render_ajuda

urlpatterns = [
    path('', render_mural, name='vagas'),
    path('candidaturas', render_candidaturas, name='candidaturas'),
    path('ajuda', render_ajuda, name='ajuda'),
]