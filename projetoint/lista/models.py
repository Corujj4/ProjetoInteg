from django.db import models

from listaprodutos.models import ListaProdutos


# Create your models here.

class Lista(models.Model):
    nome = models.CharField('nome',max_length=100,help_text='nome do produto')
    produto = models.ManyToManyField('produtos.Produtos', through='listaprodutos.ListaProdutos')


    @property
    def produtos(self):
        return ListaProdutos.objects.filter(lista=self)


    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'
        ordering = ['nome']

    def __str__(self):
        return self.nome