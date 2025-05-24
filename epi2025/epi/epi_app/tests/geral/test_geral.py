import pytest
from django.urls import reverse
from django.test import Client
from epi_app.models import Equipamentos, Colaboradores
# from django.test import TestCase --> padrão do Django

# Create your tests here.
#teste de URL:
def test_url_home():
    url = reverse('home') # Resolve o nome da URL 'home' para o caminho da URL real
    assert url == '/' # Verifica se o caminho resolvido é exatamente '/'
    #reverse('home') procura na configuração de URLs (urls.py) do projeto a URL 'home' 
    # (por exemplo, path('', views.index, name='home')) e retorna a string do caminho dessa URL.
    #O assert verifica se essa URL realmente corresponde à raiz do site ('/'). Se não, o teste falha.

#teste de requisição:
@pytest.mark.django_db
def test_url_home_200():
    client = Client()
    response = client.get(reverse('home')) # Ou client.get('/') #REVERSE só serve para URLs que existem
    assert response.status_code == 200

@pytest.mark.django_db
def test_url_inexistente_404():
    client = Client()
    response = client.get('/rota_que_nao_existe/') #reverse('xxx') não funciona com algo inexistente
    assert response.status_code == 404

# @pytest.mark.django_db
# def test_url_home_404():
#     client = Client()
#     response = client.get(reverse('home')) 
#     assert response.status_code == 404

# @pytest.mark.django_db
# def test_url_home_empty():
#     client = Client()
#     response = client.get(reverse('home'))
#     assert "A página está vazia" in response.content.decode('utf-8')
#     #professor aplicou um empty no template para testar
#     #no nosso projeto tem que ir nas páginas de listar para testar
#     #não usamos empty, usamos if mais básico

#testando modelos:
@pytest.mark.django_db
def test_url_criar_epi_200_not_empty(): #test_url_listagem tbm poderia se chamar
    Equipamentos.objects.create(nome='capacete', tipo='cabeca')
    client = Client()
    response = client.get(reverse('listagem_equipamentos')) #apesar de estarmos criando, a rota de listagem é outra
    assert "capacete" in response.content.decode('utf-8')
    assert "cabeca" in response.content.decode('utf-8')
    assert "/listagem_epi/" in response.content.decode('utf-8')
    assert "/editar_epi/1" in response.content.decode('utf-8') #testando pelo id na página de editar


@pytest.mark.django_db
def test_criar_epi_via_post():
    client = Client()
    data = {
        'nome': 'Luva de proteção',
        'tipo': 'superiores'
    }
    #O Django não impede a criação de objetos com valores inválidos nos choices
    #  se você usar .create() diretamente. Ele só valida se você usar um ModelForm ou full_clean().
    response = client.post(reverse('cadastro_equipamento'), data)
    
    # Verifica se redirecionou após o cadastro (por padrão, isso indica sucesso)
    assert response.status_code in [302, 200]

    # Verifica se o objeto foi realmente criado no banco
    epi = Equipamentos.objects.get(nome='Luva de proteção', tipo='superiores')
    assert epi.tipo == 'superiores'

@pytest.mark.django_db
def test_criar_colaborador_via_post():
    client = Client()
    data = {
        'nome': 'Jao',
        'cargo': 'administrador',
        'setor': 'vadiagem'
    }
    response = client.post(reverse('cadastro_colaborador'), data)
    assert response.status_code in [302, 200]
    #O redirect() retorna 302 (redirecionamento). ver VIEWS
    #Se for render(), retorna 200. ver VIEWS
    peao = Colaboradores.objects.get(nome='Jao', cargo='administrador', setor='vadiagem')
    assert peao.setor == 'vadiagem'

    retorno = client.get(reverse('listagem_editar'))
    assert "Jao" in retorno.content.decode('utf-8')
    #assert "mandriao" in retorno.content.decode('utf-8') --> assim não passa
    
    #Testar a edição de um EPI.
@pytest.mark.django_db
def test_edicao_epi_via_post():
     epi = Equipamentos.objects.create(nome='colete', tipo='superiores')
     client = Client()
     data = {
            'nome': 'luvas',
            'tipo': 'superiores'
        }
     response = client.post(reverse('editar_equipamento', args=[epi.id]), data)
     assert response.status_code in [302, 200]
     epi = Equipamentos.objects.get(id=epi.id)
     assert epi.tipo == 'superiores' #de novo: Django não valida choices, sóse tiver no DjangoForms
     assert epi.nome == "luvas"

    #Testar a exclusão de um EPI.

    #Testar se o template correto está sendo renderizado (usando response.template_name).