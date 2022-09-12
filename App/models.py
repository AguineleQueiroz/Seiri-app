from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Tarefa(models.Model):

    PRIORIDADE = (
        ('Alta', 'Alta'),
        ('Normal', 'Normal'),
        ('Baixa', 'Baixa'),
    )
    id = models.AutoField(primary_key=True)
    tarefa = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    data = models.DateField(null=False, blank=False)
    prioridade = models.CharField(max_length=6, null=False, choices=PRIORIDADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.tarefa


class TarefasConcluidas(models.Model):
    PRIORIDADE = (
        ('Alta', 'Alta'),
        ('Normal', 'Normal'),
        ('Baixa', 'Baixa'),
    )

    id = models.AutoField(primary_key=True)
    tarefa = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    data = models.DateField(null=False, blank=False)
    prioridade = models.CharField(max_length=6, null=False, choices=PRIORIDADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tarefa
