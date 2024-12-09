from logging import disable

from django.db import models


class Produtos(models.Model):


    nome = models.CharField('Nome', max_length=100, help_text='Nome completo do produto', unique=True  )
    quantidade = models.DecimalField('quantidade',max_digits=5, decimal_places=2, help_text='quantidade do produtos em estoque')
    descricao = models.TextField('Descrição', max_length=300, help_text='Descricao e observações do produto')
    tipo_de_produto = models.CharField('Tipo', max_length=10, help_text='Tipo de produto', null=False, blank=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome

    def deletar(self):
        self.delete()


class Remedio(Produtos):

    validade = models.CharField('Validade',max_length=100,help_text='Validade do remedio.')

    def save(self, *args, **kwargs):
        self.tipo_de_produto = 'REMEDIO'
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'remedio'
        verbose_name_plural = 'remedios'

    def __str__(self):
        return super().nome

class Roupa(Produtos):

    genero = models.CharField('Genero',max_length=100,help_text='masculino ou feminino.')
    tamanho = models.CharField('Tamanho',max_length=100,help_text='tamanho da peça.')

    def save(self, *args, **kwargs):
        self.tipo_de_produto = 'ROUPA'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'roupa'
        verbose_name_plural = 'roupas'

    def __str__(self):
        return super().nome


class Mantimento(Produtos):

    validade = models.CharField('Validade', max_length=100, help_text='Validade do mantimento.')
    categoria = models.CharField('Categoria', max_length=100, help_text='Categoria do mantimento  (liquido ou solido ).')

    def save(self, *args, **kwargs):
        self.tipo_de_produto = 'MANTIMENTO'
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'mantimento'
        verbose_name_plural = 'mantimentos'

    def __str__(self):
        return super().nome