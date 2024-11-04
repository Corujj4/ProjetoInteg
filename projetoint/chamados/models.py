from django.db import models


class Chamado(models.Model):

    unidade = models.DecimalField('unidade',max_digits=5, decimal_places=2, help_text='unidade de items do chamado')
    quantidade = models.DecimalField('Quantidade',max_digits=5, decimal_places=2, help_text='quantidade do produtos em estoque')
    prioridade = models.TextField('Prioridade', max_length=300, help_text='Nivel de urgencia do chamado')
    situacao = models.TextField('Situacao', max_length=300, help_text='Estado do chamado')

    class Meta:
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'

    def __str__(self):
        return self.id
