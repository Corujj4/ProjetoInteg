from django.db import models


class Chamado(models.Model):
    PRIORIDADE_OPCOES = (
        ('A', 'ALTA'),
        ('M', 'MEDIA'),
        ('B', 'BAIXA'),
    )


    unidade = models.DecimalField('unidade',max_digits=5, decimal_places=2, help_text='unidade de items do chamado')
    produto = models.ForeignKey('produtos.Produtos',verbose_name='Produto',help_text='Produto a ser solicitado', on_delete=models.SET_NULL,null=True,blank=True)
    prioridade = models.CharField('prioridade',max_length=1, help_text='Prioridade do chamado', choices=PRIORIDADE_OPCOES)
    funcionario = models.ForeignKey('funcionario.Funcionario', verbose_name='Funcionario', help_text='Nome do funcionario',on_delete=models.PROTECT )
    vitima = models.ForeignKey('vitima.Vitima', verbose_name='Vitima',help_text='Nome da vitima', on_delete=models.PROTECT )
    status = models.CharField('Status', max_length=1, help_text='Status do chamado', default='Em andamento')
    descricao = models.TextField('Descricao',max_length=500, help_text='Descricao do chamado')




    class Meta:
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'
        ordering = ['-prioridade']


