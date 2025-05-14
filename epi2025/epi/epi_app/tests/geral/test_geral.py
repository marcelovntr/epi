import pytest
from django.urls import reverse
from django.test import Client
from epi_app.models import Equipamentos
# from django.test import TestCase --> padrão do Django

# Create your tests here.
def test_url_home():
    url = reverse('home') # Resolve o nome da URL 'home' para o caminho da URL real
    assert url == '/' # Verifica se o caminho resolvido é exatamente '/'
    #reverse('home') procura na configuração de URLs (urls.py) do projeto a URL 'home' 
    # (por exemplo, path('', views.index, name='home')) e retorna a string do caminho dessa URL.
    #O assert verifica se essa URL realmente corresponde à raiz do site ('/'). Se não, o teste falha.

@pytest.mark.django_db
def test_url_home_200():
    client = Client()
    response = client.get(reverse('home')) # Ou client.get('/')
    assert response.status_code == 200

# @pytest.mark.django_db
# def test_url_home_empty():
#     client = Client()
#     response = client.get(reverse('home'))
#     assert "A página está vazia" in response.content.decode('utf-8')
#     #professor aplicou um empty no template para testar
#     #no nosso projeto tem que ir nas páginas de listar para testar
#     #não usamos empty, usamos if mais básico

@pytest.mark.django_db
def test_url_criar_epi_200_not_empty(): #test_url_listagem tbm poderia se chamar
    Equipamentos.objects.create(nome='capacete', tipo='cabeca')
    client = Client()
    response = client.get(reverse('listagem_equipamentos')) #apesar de estarmos criando, a rota de listagem é outra
    assert "capacete" in response.content.decode('utf-8')
    assert "cabeca" in response.content.decode('utf-8')
    assert "/listagem_epi/" in response.content.decode('utf-8')
    assert "/editar_epi/1" in response.content.decode('utf-8')