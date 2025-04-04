
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro_colaborador, name='cadastro_colaborador'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('editar/', views.editar_colaborador, name='editar_colaborador'),

]
