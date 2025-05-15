from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from epi_app.models import Colaboradores, Equipamentos, Controle, Usuarios
from django.views.decorators.http import require_POST
from datetime import datetime
from django.db.models import Q, ProtectedError

def home(request):
    return render(request, 'epi_app/pages/home.html') 