# Guia Passo-a-Passo para Criar um Projeto Django

1. Configuração do Ambiente Virtual

Antes de iniciar o desenvolvimento, é recomendado criar um ambiente virtual para gerenciar dependências.

Criar o ambiente virtual:

 ```bash
pip install virtualenv
python -m venv .venv
 ```

Atualizar o gerenciador de pacotes:
```bash
python.exe -m pip install --upgrade pip
```
Ativar o ambiente virtual (Certifique-se de estar na pasta correta):
```bash
.\.venv\Scripts\Activate.ps1  # Para Windows (PowerShell)
source .venv/bin/activate       # Para Linux/Mac
```
2. Instalação do Django

Após ativar o ambiente virtual, instale o Django:
```bash
pip install django
```
3. Criando um Projeto Django
```bash
django-admin startproject oremos
```
Observação: Esse comando cria uma pasta oremos, dentro dela haverá outra pasta oremos contendo os arquivos principais do projeto.

4. Rodando o Servidor de Desenvolvimento

Dentro da pasta do projeto, execute:
```bash
python manage.py runserver
```
Nota: No Windows, utilize python ao invés de python3.

Para visualizar os comandos disponíveis:

```bash
python manage.py --help
```
5. Criando um Aplicativo Django

Dentro da pasta do projeto (onde está manage.py), execute:
```bash
python manage.py startapp app_site
```
Isso criará uma nova pasta app_site, contendo a estrutura do aplicativo.

Estrutura de Diretórios do app_site:

migrations/: Gerencia as alterações no banco de dados (não necessário modificar manualmente).

admin.py: Gerencia o painel administrativo do Django.

apps.py: Configurações do aplicativo (normalmente não requer modificações).

models.py: Define os modelos de banco de dados (semelhante ao Sequelize no Node.js).

tests.py: Utilizado para testes (abordado futuramente).

views.py: Lida com a lógica de exibição da aplicação.

6. Registrando o Aplicativo no Projeto

Abra settings.py na pasta do projeto e adicione o nome do aplicativo à lista INSTALLED_APPS:

INSTALLED_APPS = [
    ...
    'app_site',
]

7. Configuração de Rotas (URLs)

No Arquivo urls.py do Projeto (oremos/urls.py):

Adicione include às importações:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_site.urls')),  # Redireciona para as rotas do app
]

Criando urls.py Dentro de app_site

Crie um arquivo urls.py dentro da pasta app_site e adicione:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('sobre/', views.sobre),
]

8. Criando as Views

No arquivo views.py dentro de app_site, crie as funções de exibição:

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

9. Criando os Templates

Crie uma pasta chamada templates dentro de app_site. Dentro dela, crie os arquivos:

index.html

sobre.html


10. Configurando Arquivos Estáticos (CSS, JS, etc.)

Crie uma pasta static dentro de app_site:
```bash
mkdir app_site/static/css
mkdir app_site/static/js
```
No HTML, carregar os arquivos estáticos

Dentro dos templates (index.html, sobre.html, etc.), adicione no topo:

{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">

No settings.py, adicione a configuração para arquivos estáticos:

from pathlib import Path
import os

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

11. Executando o Servidor Novamente

Após realizar as configurações, rode o servidor novamente:

python manage.py runserver

Acesse no navegador: http://127.0.0.1:8000