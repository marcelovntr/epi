from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from epi_app.models import Colaboradores, Equipamentos, Controle, Usuarios
from django.views.decorators.http import require_POST
from datetime import datetime
from django.db.models import Q, ProtectedError

def cadastro_equipamento(request):
    if request.method == 'GET':
        return render(request, 'epi_app/pages/cadastro_epi.html')

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        tipo = request.POST.get('tipo', '').strip()

        if not nome or not tipo:
            messages.error(request, 'Ambos campos são obrigatórios.')
            return render(request, 'epi_app/pages/cadastro_epi.html')
    
        equipamento = Equipamentos.objects.create(nome=nome, tipo=tipo)
        messages.success(request, f'Equipamento: {nome} cadastrado com sucesso!')
        return redirect('cadastro_equipamento')
    return render(request, 'epi_app/pages/cadastro_epi.html', context={'equipamento': equipamento})

def listagem_equipamentos(request):
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        lista_epi = Equipamentos.objects.filter(
            # | é OR
            Q(nome__icontains=pesquisa) |
            Q(tipo__icontains=pesquisa)
            )
        # if not lista_epi.exists():
        #     messages.error(request, 'Equipamento ou tipo não encontrado.')
        if len(lista_epi) == 0:
            messages.error(request, 'Equipamento ou tipo não encontrado.')
            lista_epi = Equipamentos.objects.all()
    else:
        lista_epi = Equipamentos.objects.all()
    return render(request, 'epi_app/pages/listagem_epi.html', context={'epis': lista_epi, 'pesquisa': pesquisa})

@require_POST
def deletar_equipamento(request, id):
    equipamento_encontrado = get_object_or_404(Equipamentos, id=id)
    # equipamento_encontrado = Equipamentos.objects.get(id=id)
    equipamento_encontrado.delete()
    return redirect('listagem_equipamentos')

def editar_equipamento(request, id):
    #seria melhor aqui: equipamento_por_id = Equipamentos.objects.get(id=id)
    if request.method == 'GET':
        equipamento_por_id = Equipamentos.objects.get(id=id)
        return render(request, 'epi_app/pages/editar_epi.html', context={'epi': equipamento_por_id})
    
    equipamento_por_id = Equipamentos.objects.get(id=id)
    nome = request.POST.get('nome')
    tipo = request.POST.get('tipo')
    
    if not nome or not tipo:
        messages.error(request, 'Ambos campos são obrigatórios.')
        return render(request, 'epi_app/pages/editar_epi.html', context={'epi': equipamento_por_id})
    
    Equipamentos.objects.filter(id=id).update(nome=nome, tipo=tipo)
    messages.success(request, f'Dados do equipamento: {nome} atualizados com sucesso!')
    return redirect('listagem_equipamentos')
