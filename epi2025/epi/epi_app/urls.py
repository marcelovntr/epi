
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro_colaborador, name='cadastro_colaborador'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('editar/<int:id>', views.editar_colaborador, name='editar_colaborador'),
    path('listagem_editar/', views.listagem_editar, name='listagem_editar'),
    path('deletar/<int:id>', views.deletar_colaborador, name='deletar_colaborador'),

]
