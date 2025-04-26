from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Colaboradores, Equipamentos, Controle, Usuarios
from django.views.decorators.http import require_POST
from datetime import datetime
from django.db.models import Q

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
    colaborador_encontrado.delete()
    return redirect('listagem_editar') 

def listagem_editar(request):
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        lista_colaboradores = Colaboradores.objects.filter(
            Q(nome__icontains=pesquisa) |
            Q(setor__icontains=pesquisa) |
            Q(cargo__icontains=pesquisa)
            )
        if len(lista_colaboradores) == 0:
            #ou: lista_colaboradores.count() == 0:
            messages.error(request, 'Nenhum colaborador encontrado com esse nome.')
            lista_colaboradores = Colaboradores.objects.all()
    else:
        lista_colaboradores = Colaboradores.objects.all()
    return render(request, 'epi_app/pages/listagem_editar.html', 
                  context={'colaboradores': lista_colaboradores, 'pesquisa': pesquisa})


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

##################CONTROLE#######################

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

###########LOGIN E USUÁRIOS################
def login(request):
# salvar na session manualmente???
#POST???

#  verificar senha:   
# from django.contrib.auth.hashers import check_password
# usuario = Usuarios.objects.get(email='teste@teste.com')
# check_password('senha_digitada', usuario.senha)

    return render(request, 'epi_app/pages/login.html')

def cadastrar_usuario(request):
    if request.method == 'GET':
        return render(request, 'epi_app/pages/cadastro_usuario.html')

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        cpf = request.POST.get('cpf', '').strip()   #converter???
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '').strip()

        if not nome or not cpf or not email or not senha:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'epi_app/pages/cadastro_usuario.html')

        try:
            cpf = int(cpf)
        except ValueError:
            messages.error(request, 'O CPF deve conter apenas números.')
            return render(request, 'epi_app/pages/cadastro_usuario.html')

        if len(senha) < 8:
            messages.error(request, 'A senha deve conter pelo menos 8 caracteres.')
            return render(request, 'epi_app/pages/cadastro_usuario.html')

        if Usuarios.objects.filter(email=email).exists() or Usuarios.objects.filter(cpf=cpf).exists():
            messages.error(request, 'Email ou CPF já cadastrados.')
            return render(request, 'epi_app/pages/cadastro_usuario.html')

        usuario = Usuarios.objects.create(nome=nome, cpf=cpf, email=email, senha=senha)
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('cadastro_usuario')    
    return render(request, 'epi_app/pages/cadastro_usuario.html', context={'usuario': usuario})