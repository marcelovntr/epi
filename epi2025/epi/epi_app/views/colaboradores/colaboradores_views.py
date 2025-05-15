from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from epi_app.models import Colaboradores, Equipamentos, Controle, Usuarios
from django.views.decorators.http import require_POST
from datetime import datetime
from django.db.models import Q, ProtectedError

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
    #poderia antes: colaborador_por_id = get_object_or_404(Colaboradores, id=id)
    if request.method == 'GET':
        #aí não necessitaria esse:
        colaborador_por_id = Colaboradores.objects.get(id=id)
        return render(request, 'epi_app/pages/editar.html', context={'colaborador': colaborador_por_id})
    
    colaborador_por_id = Colaboradores.objects.get(id=id)  
    nome = request.POST.get('nome')
    cargo = request.POST.get('cargo')
    setor = request.POST.get('setor')
    
    if not nome or not cargo or not setor:
        messages.error(request, 'Todos os campos são obrigatórios.')
        return render(request, 'epi_app/pages/editar.html', context={'colaborador': colaborador_por_id})

    # colaborador_por_id.nome = nome
    # colaborador_por_id.cargo = cargo
    # colaborador_por_id.setor = setor
    # colaborador_por_id.save()
    Colaboradores.objects.filter(id=id).update(nome=nome, cargo=cargo, setor=setor)
    messages.success(request, f'Dados do colaborador: {nome} atualizados com sucesso!')
    #return render(request, 'epi_app/pages/editar.html', context={'colaborador': colaborador_por_id})
    return redirect('listagem_editar')  
   

@require_POST
def deletar_colaborador(request, id):
    colaborador_encontrado = get_object_or_404(Colaboradores, id=id)
    # colaborador_encontrado = Colaboradores.objects.get(id=id)
    try:
        colaborador_encontrado.delete()
        messages.success(request, f'Colaborador "{colaborador_encontrado.nome}" deletado com sucesso!')
    except ProtectedError:
        messages.error(
            request,
            f'Não foi possível deletar o colaborador "{colaborador_encontrado.nome}" porque ele está vinculado a registros de controle.'
        )
    except Exception as e:
        messages.error(request, f'Erro ao deletar colaborador "{colaborador_encontrado.nome}": {str(e)}')
    # colaborador_encontrado.delete()
    return redirect('listagem_editar') 

def listagem_editar(request):
    pesquisa = request.GET.get('pesquisa')
    lista_colaboradores = None #ou []
    lista_encontrados = None #ou []
    #None é "igual" ao Null em JavaScript
    if pesquisa:
        lista_encontrados = Colaboradores.objects.filter(
            Q(nome__icontains=pesquisa) |
            Q(setor__icontains=pesquisa) |
            Q(cargo__icontains=pesquisa)
            )
        if not lista_encontrados.exists():
            #ou: if len(lista_encontrados) == 0:
            #ou: lista_colaboradores.count() == 0:
            messages.error(request, 'Nenhum colaborador encontrado com esse nome.')
           
    else:
        lista_colaboradores = Colaboradores.objects.all()
    return render(request, 'epi_app/pages/listagem_editar.html', 
                  context={'colaboradores': lista_colaboradores, 'encontrados': lista_encontrados, 'pesquisa': pesquisa})

