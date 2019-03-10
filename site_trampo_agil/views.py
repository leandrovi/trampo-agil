from django.shortcuts import render

# Create your views here.
def render_home(request):
    return render(request, 'home.html')

def render_candidatos(request):
    return render(request, 'candidatos.html')

def render_empresas(request):
    return render(request, 'empresas.html')

def render_login_candidatos(request):
    return render(request, 'login_candidatos.html')
    
def render_login_empresas(request):
    return render(request, 'login_empresas.html')

def render_mural_vagas(request):
    return render(request, 'mural_vagas.html')