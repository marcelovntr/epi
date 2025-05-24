
# 🛠️ Passo a Passo: Projeto Django - CRUD Básico

## 🚀 Iniciando o Projeto

1. (Opcional) Criar ambiente virtual:
   ```bash
   python -m venv .venv
   ```

2. Comandos iniciais:
   ```bash
   pip install django
   django-admin startproject projetinho
   cd projetinho  # não esquecer!
   python manage.py startapp projetinho_app
   ```

## ⚙️ Configurando `settings.py`

- Adicionar o app ao `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
       ...
       "projetinho_app",
   ]
   ```

## 🌐 Configurando URLs

### 1️⃣ URLs do Projeto (arquivo `projetinho/urls.py`)

- Importar `include`:
   ```python
   from django.urls import path, include
   ```

- Declarar as rotas:
   ```python
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('projetinho_app.urls')),
   ]
   ```

### 2️⃣ URLs do App (arquivo `projetinho_app/urls.py`)

- Criar o arquivo `urls.py` dentro do app e adicionar:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.home, name='home'),
       path('demais/', views.demais, name='demais'),
   ]
   ```

## 🧱 Models

- Em `projetinho_app/models.py`:
   ```python
   from django.db import models

   class Item(models.Model):
       nome = models.CharField(max_length=100)
       descricao = models.CharField(max_length=200)

       def __str__(self):
           return self.nome + ' - ' + self.descricao
   ```

## 🖼️ Templates

- Criar a pasta `templates/` com os seguintes arquivos:
  - `index.html` (ou `home.html`)
  - `criar.html`
  - `listar.html`
  - `editar.html` (parecido com `criar`, mas com valores preenchidos)

- Usar template base (`base.html`) para reaproveitar layout

- Sintaxe Jinja/Django:
   ```django
   {% extends 'base.html' %}
   {% load static %}

   {% block title %}Título{% endblock %}

   {% block content %}
   Conteúdo aqui
   {% endblock %}
   ```

## 🎨 Static

- Criar a pasta `static/` (no mesmo nível da pasta `templates/`)
  - Subpastas sugeridas:
    - `css/`
    - `js/`
    - `img/`

## 🧠 Views

- Exemplo de view simples:
   ```python
   from django.shortcuts import render

   def home(request):
       return render(request, 'home.html')
   ```

- Outras funções esperadas:
  - `criar()`
  - `listar()`
  - `editar()`
