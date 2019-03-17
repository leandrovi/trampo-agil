from django.shortcuts import render
from site_trampo_agil.models import Candidato, Empresa
from site_trampo_agil.forms import LoginCriarForm

# Create your views here.
def render_home(request):
    return render(request, 'home.html')

def render_candidatos(request):
    return render(request, 'candidatos.html')

def render_empresas(request):
    return render(request, 'empresas.html')

def render_login_candidatos(request):
    formulario = LoginCriarForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        formulario = LoginCriarForm()

    context = {
        'form': formulario
    }

    return render(request, 'login_candidatos.html', context)
    
def render_login_empresas(request):
    return render(request, 'login_empresas.html')

def render_mural_vagas(request):
    return render(request, 'mural_vagas.html')

