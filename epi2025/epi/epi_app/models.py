from django.db import models
# cpf = models.CharField(max_length=11)
# email = models.EmailField()
# telefone = models.CharField(max_length=20)
# Create your models here.
class Colaboradores(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Colaborador({self.nome}, {self.cargo}, {self.setor})"
