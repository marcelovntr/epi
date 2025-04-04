from django.shortcuts import render
from .models import Colaboradores

# Create your views here.
def home(request):
    return render(request, 'epi_app/pages/home.html') 
def cadastro_colaborador(request):
    if request.method == 'GET':
        return render(request, 'epi_app/pages/cadastro.html')
    nome = request.POST.get('nome')
    cargo = request.POST.get('cargo')    
    setor = request.POST.get('setor')
    colaborador = Colaboradores.objects.create(nome=nome, cargo=cargo, setor=setor)
    return render(request, 'epi_app/pages/cadastro.html', context={'colaborador': colaborador})

def relatorios(request):
    lista_colaboradores = Colaboradores.objects.all()
    return render(request, 'epi_app/pages/relatorios.html', context={'colaboradores': lista_colaboradores})

def editar_colaborador(request):
    return render(request, 'epi_app/pages/editar.html')