from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Colaboradores, Equipamentos, Controle
from django.views.decorators.http import require_POST
from datetime import datetime

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


###############EQUIPAMENTOS###############

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
    lista_epi = Equipamentos.objects.all()
    return render(request, 'epi_app/pages/listagem_epi.html', context={'epis': lista_epi})

@require_POST
def deletar_equipamento(request, id):
    equipamento_encontrado = get_object_or_404(Equipamentos, id=id)
    # equipamento_encontrado = Equipamentos.objects.get(id=id)
    equipamento_encontrado.delete()
    return redirect('listagem_equipamentos')

def editar_equipamento(request, id):
    if request.method == 'GET':
        equipamento_por_id = Equipamentos.objects.get(id=id)
        return render(request, 'epi_app/pages/editar_epi.html', context={'epi': equipamento_por_id})
    nome = request.POST.get('nome')
    tipo = request.POST.get('tipo')
    Equipamentos.objects.filter(id=id).update(nome=nome, tipo=tipo)
    return redirect('listagem_equipamentos')

##################CONTROLE#######################

def cadastrar_controle(request):
    if request.method == 'GET':
        return render(request, 'epi_app/pages/controle.html')
    
    if request.method == 'POST':
        equipamento = request.POST.get('equipamento', '').strip()
        colaborador = request.POST.get('colaborador', '').strip()
        data_emprestimo = request.POST.get('data-emprestimo', '').strip()
        data_prevista = request.POST.get('data-prevista', '').strip()
        status = request.POST.get('status', '').strip()
        condicoes = request.POST.get('condicoes', '').strip()
        data_devolucao = request.POST.get('data-devolucao', '').strip()
        observacoes = request.POST.get('observacoes', '').strip()

        if not equipamento or not colaborador or not data_emprestimo or not data_prevista or not status or not condicoes:
            messages.error(request, 'Preencha os campos obrigatórios.')
            return render(request, 'epi_app/pages/controle.html')
        
        try:
            data_emprestimo = datetime.strptime(data_emprestimo, '%Y-%m-%d').date()
            data_prevista = datetime.strptime(data_prevista, '%Y-%m-%d').date()
            data_devolucao = datetime.strptime(data_devolucao, '%Y-%m-%d').date() if data_devolucao else None
        except ValueError:
            messages.error(request, 'Formato de data inválido.')
            return render(request, 'epi_app/pages/controle.html')
        
        controle = Controle.objects.create(
            equipamento= equipamento,
            colaborador= colaborador,
            data_emprestimo= data_emprestimo,
            data_prevista= data_prevista,
            status= status,
            condicoes= condicoes,
            data_devolucao= data_devolucao,
            observacoes= observacoes
        )
        messages.success(request, f'Controle: {equipamento} cadastrado com sucesso!')
        return redirect('cadastrar_controle')
    return render(request, 'epi_app/pages/controle.html', context={'controle': controle})