from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'epi_app/pages/home.html')
def cadastro_colaborador(request):
    return render(request, 'epi_app/pages/cadastro.html')

def relatorios(request):
    return render(request, 'epi_app/pages/relatorios.html')

def editar_colaborador(request):
    return render(request, 'epi_app/pages/editar.html')