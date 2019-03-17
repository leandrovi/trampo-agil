from django.shortcuts import render
from mural_vagas.models import Vaga

# Create your views here.
def render_mural(request):
    vagas = Vaga.objects.all()
    context = {
        'vagas': vagas
    }
    return render(request, 'base-mural.html', context)

def render_candidaturas(request):
    return render(request, 'candidaturas.html')

def render_ajuda(request):
    return render(request, 'ajuda.html')