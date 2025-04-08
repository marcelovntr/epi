from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Colaboradores
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    return render(request, 'epi_app/pages/home.html') 
def cadastro_colaborador(request):
    if request.method == 'GET':
        return render(request, 'epi_app/pages/cadastro.html')
    
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        cargo = request.POST.get('cargo', '').strip()    
        setor = request.POST.get('setor', '').strip()

        if not nome or not cargo or not setor:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'epi_app/pages/cadastro.html')
    
        colaborador = Colaboradores.objects.create(nome=nome, cargo=cargo, setor=setor)
        messages.success(request, f'Colaborador: {nome} cadastrado com sucesso!')
        return redirect('cadastro_colaborador')
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

@require_POST
def deletar_colaborador(request, id):
    colaborador_encontrado = get_object_or_404(Colaboradores, id=id)
    # colaborador_encontrado = Colaboradores.objects.get(id=id)
    colaborador_encontrado.delete()
    return redirect('listagem_editar') 

def listagem_editar(request):
    lista_colaboradores = Colaboradores.objects.all()
    return render(request, 'epi_app/pages/listagem_editar.html', context={'colaboradores': lista_colaboradores})