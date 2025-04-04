from django.shortcuts import render, redirect
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
    return render(request, 'epi_app/pages/relatorios.html')

def editar_colaborador(request, id):
    if request.method == 'GET':
        colaborador_por_id = Colaboradores.objects.get(id=id)
        return render(request, 'epi_app/pages/editar.html', context={'colaborador': colaborador_por_id})
    nome = request.POST.get('nome')
    cargo = request.POST.get('cargo')
    setor = request.POST.get('setor')
    Colaboradores.objects.filter(id=id).update(nome=nome, cargo=cargo, setor=setor)
    return redirect('listagem_editar')

def deletar_colaborador(request, id):
    colaborador_encontrado = Colaboradores.objects.get(id=id)
    colaborador_encontrado.delete()
    return redirect('listagem_editar') 

def listagem_editar(request):
    lista_colaboradores = Colaboradores.objects.all()
    return render(request, 'epi_app/pages/listagem_editar.html', context={'colaboradores': lista_colaboradores})