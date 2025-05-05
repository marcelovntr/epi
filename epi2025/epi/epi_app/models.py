from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.
class Colaboradores(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Colaborador({self.nome}, {self.cargo}, {self.setor})"
    
class Equipamentos(models.Model):
    TIPOS_EPI = [
        ('cabeca', 'Proteção da cabeça'),
        ('auditiva', 'Proteção auditiva'),
        ('respiratoria', 'Proteção respiratória'),
        ('ocular_facial', 'Proteção ocular e facial'),
        ('superiores', 'Proteção dos membros superiores'),
        ('inferiores', 'Proteção dos membros inferiores'),
        ('quedas', 'Proteção contra quedas'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_EPI)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"EPI({self.nome} - {self.get_tipo_display()})"

class Controle(models.Model):
    TIPO_STATUS = [
        ('emprestado', 'Emprestado'),
        ('em-uso', 'Em uso'),
        ('devolvido', 'Devolvido'),
        ('perdido', 'Perdido'),
        ('danificado', 'Danificado'),
        ('fornecido', 'Fornecido'),
    ]
    equipamento = models.ForeignKey(Equipamentos, on_delete=models.PROTECT)
    colaborador = models.ForeignKey(Colaboradores, on_delete=models.PROTECT)
    data_emprestimo = models.DateField()
    data_prevista = models.DateField()
    status = models.CharField(max_length=20, choices=TIPO_STATUS)
    condicoes = models.TextField()
    data_devolucao = models.DateField()
    observacoes = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)


#class Usuarios(BaseUserManager, AbstractBaseUser):
class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # cpf = models.CharField(max_length=11, unique=True)
    senha = models.CharField(
        #maior???
        max_length=128, 
        validators=[MinLengthValidator(8)])
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     # Só criptografa se ainda não estiver criptografada
    #     if not self.senha.startswith('pbkdf2_'):
    #         self.senha = make_password(self.senha)
    #     super().save(*args, **kwargs)
    def __str__(self):
        return f"Usuario({self.nome}, {self.email})"
