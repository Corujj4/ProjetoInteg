from django.db import models
from pessoa.models import Pessoa


class Funcionario(Pessoa):
    hrs = models.CharField('Horas',max_length=100,help_text='Horas de Trabalho')
    funcao = models.CharField('Função', max_length=35, help_text='Função na empresa')
    class Meta:
        verbose_name = 'Horas'
        verbose_name_plural = 'Horas de Trabalho Pro dia'

    def __str__(self):
        return super().nome
