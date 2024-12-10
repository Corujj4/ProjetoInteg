from django.db import models

# Create your models here.
class ListaProdutos(models.Model):

    lista = models.ForeignKey('lista.Lista',verbose_name='lista',help_text='nome da lista', related_name='lista', on_delete=models.CASCADE)
    produto = models.ForeignKey('produtos.Produtos',verbose_name='produto',help_text='nome da produto', related_name='produtos', on_delete=models.CASCADE)
    quantidade = models.IntegerField(verbose_name='quantidade', default=0)

    class Meta:
        verbose_name = 'lista de produtos'
        verbose_name_plural = 'listas de produtos'
        ordering = ['quantidade']

    def __str__(self):
        return f'{self.produto}'