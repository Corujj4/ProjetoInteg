from django.db import models
from pessoa.models import Pessoa


class Vitima(Pessoa):
    necessidade = models.CharField('Necessidade',max_length=100,help_text='Descricao de necessidade')

    class Meta:
        verbose_name = 'vitima'
        verbose_name_plural = 'vitimas'

    def __str__(self):
        return super().nome
