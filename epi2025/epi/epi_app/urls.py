
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro_colaborador, name='cadastro_colaborador'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('editar/<int:id>', views.editar_colaborador, name='editar_colaborador'),
    path('listagem_editar/', views.listagem_editar, name='listagem_editar'),
    path('deletar/<int:id>', views.deletar_colaborador, name='deletar_colaborador'),

    path('cadastro_epi/', views.cadastro_equipamento, name='cadastro_equipamento'),
    path('editar_epi/<int:id>', views.editar_equipamento, name='editar_equipamento'),
    path('listagem_epi/', views.listagem_equipamentos, name='listagem_equipamentos'),
    path('deletar_epi/<int:id>', views.deletar_equipamento, name='deletar_equipamento'),

    path('controle/', views.cadastrar_controle, name='cadastrar_controle'),
    path('listagem_controle/', views.listar_controle, name='listar_controle'),

    path('login/', views.login, name='login'),

]
