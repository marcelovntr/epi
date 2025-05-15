from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from epi_app.models import Colaboradores, Equipamentos, Controle, Usuarios
from django.views.decorators.http import require_POST
from datetime import datetime
from django.db.models import Q, ProtectedError
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