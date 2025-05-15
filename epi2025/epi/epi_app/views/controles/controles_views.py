from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from epi_app.models import Colaboradores, Equipamentos, Controle, Usuarios
from django.views.decorators.http import require_POST
from datetime import datetime
from django.db.models import Q, ProtectedError

def cadastrar_controle(request):
    colaboradores = Colaboradores.objects.all()
    equipamentos = Equipamentos.objects.all()
    if request.method == 'GET':
        return render(request, 'epi_app/pages/controle.html',context={'colaboradores': colaboradores, 'equipamentos': equipamentos})
    
    if request.method == 'POST':
        equipamento = request.POST.get('epi', '').strip()
        colaborador = request.POST.get('colaborador', '').strip()
        data_emprestimo = request.POST.get('data-emprestimo', '').strip()
        data_prevista = request.POST.get('data-prevista', '').strip()
        status = request.POST.get('status', '').strip()
        condicoes = request.POST.get('condicoes', '').strip()
        data_devolucao = request.POST.get('data-devolucao', '').strip()
        observacoes = request.POST.get('observacoes', '').strip()

        if not equipamento or not colaborador or not data_emprestimo or not data_prevista or not status or not condicoes:
            messages.error(request, 'Preencha os campos obrigatórios.')
            return render(request, 'epi_app/pages/controle.html', context={
                'colaboradores': colaboradores,
                'equipamentos': equipamentos
        })
        try:
            data_emprestimo = datetime.strptime(data_emprestimo, '%Y-%m-%d').date()
            data_prevista = datetime.strptime(data_prevista, '%Y-%m-%d').date()
            # if data_devolucao: 
            data_devolucao = datetime.strptime(data_devolucao, '%Y-%m-%d').date()
           
            if data_emprestimo > data_prevista or data_emprestimo > data_devolucao:
                messages.error(request, 'A data de empréstimo deve ser menor que a data prevista e a data de devolução.')
                return render(request, 'epi_app/pages/controle.html', context={
                    'colaboradores': colaboradores,
                    'equipamentos': equipamentos
                })

            equipamento = Equipamentos.objects.get(id=int(equipamento))
            colaborador = Colaboradores.objects.get(id=int(colaborador))
        
        except (ValueError, Equipamentos.DoesNotExist, Colaboradores.DoesNotExist):
            messages.error(request, 'Erro ao processar os dados. Verifique os IDs fornecidos.')
            return render(request, 'epi_app/pages/controle.html', context={
                'colaboradores': colaboradores,
                'equipamentos': equipamentos
            })
        
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
        messages.success(request, f'Controle: {equipamento.nome} do colaborador: {colaborador.nome} cadastrado com sucesso!')
        return redirect('cadastrar_controle')
    return render(request, 'epi_app/pages/controle.html', context={'controle': controle,
          'colaboradores': colaboradores,
        'equipamentos': equipamentos})

def listar_controle(request):
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        lista_controle = Controle.objects.filter(
            # | é OR
            Q(colaborador__nome__icontains=pesquisa) |
            Q(equipamento__nome__icontains=pesquisa) |
            Q(status__icontains=pesquisa)
            )
        if len(lista_controle) == 0:
            messages.error(request, 'Colaborador/equipamento/status não encontrado.')
            lista_controle = Controle.objects.all()
    else:
        lista_controle = Controle.objects.all()
    return render(request, 'epi_app/pages/listagem_controle.html', context={'controladoria': lista_controle, 'pesquisa': pesquisa})

def editar_controle(request, id):
    
    if request.method == 'GET':
        controle_por_id = Controle.objects.get(id=id)
        colaboradores = Colaboradores.objects.all()
        equipamentos = Equipamentos.objects.all()
        return render(request, 'epi_app/pages/controle_editar.html', context={'controle': controle_por_id, 'colaboradores': colaboradores, 'equipamentos': equipamentos})
    
    controle_por_id = Controle.objects.get(id=id)
    # equipamento = request.POST.get('epi', '').strip()
    # colaborador = request.POST.get('colaborador', '').strip()
    # data_emprestimo = request.POST.get('data-emprestimo', '').strip()
    # data_prevista = request.POST.get('data-prevista', '').strip()
    status = request.POST.get('status', '').strip()
    condicoes = request.POST.get('condicoes', '').strip()
    # data_devolucao = request.POST.get('data-devolucao', '').strip()
    observacoes = request.POST.get('observacoes', '').strip()
    Controle.objects.filter(id=id).update(status=status, condicoes=condicoes, observacoes=observacoes)
    messages.success(request, f'Controle: {controle_por_id.equipamento.nome} do colaborador: {controle_por_id.colaborador.nome} atualizado com sucesso!')
    return redirect('listar_controle')

def deletar_controle(request, id):
    controle = Controle.objects.get(id=id)
    controle.delete()
    messages.success(request, f'Controle: {controle.equipamento.nome} do colaborador: {controle.colaborador.nome} deletado com sucesso!')
    return redirect('listar_controle')