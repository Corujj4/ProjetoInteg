from django.db import models


class Produtos(models.Model):
    nome = models.CharField('Nome', max_length=100, help_text='Nome completo do produto')
    descricao = models.TextField('Descrição', max_length=300, help_text='Descrição e observações do produto')
    tipo_de_produto = models.CharField('Tipo', max_length=10, help_text='Tipo de produto', null=False, blank=True)

    def deletar(self):
        self.delete()

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


class Remedio(Produtos):
    validade = models.CharField('Validade', max_length=100, help_text='Validade do remédio.')
    gramatura = models.CharField('Gramatura', max_length=5, help_text='Gramas do remédio')
    quantidade = models.IntegerField('Quantidade', help_text='Quantidade do produto em estoque', null=False, default=0)



    def save(self, *args, **kwargs):
        self.tipo_de_produto = 'REMEDIO'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Remédio'
        verbose_name_plural = 'Remédios'
        ordering = ['-validade']

    def __str__(self):
        return super().__str__()  # Correção aqui


class Roupa(Produtos):
    genero = models.CharField('Gênero', max_length=100, help_text='Masculino ou feminino.')
    tamanho = models.CharField('Tamanho', max_length=100, help_text='Tamanho da peça.')
    quantidade = models.IntegerField('Quantidade', help_text='Quantidade do produto em estoque', null=False, default=0)



    def save(self, *args, **kwargs):
        self.tipo_de_produto = 'ROUPA'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Roupa'
        verbose_name_plural = 'Roupas'

    def __str__(self):
        return super().__str__()  # Correção aqui


class Mantimento(Produtos):
    validade = models.CharField('Validade', max_length=100, help_text='Validade do mantimento.')
    categoria = models.CharField('Categoria', max_length=100, help_text='Categoria do mantimento (líquido ou sólido).')
    quantidade = models.IntegerField('Quantidade', help_text='Quantidade do produto em estoque', null=False, default=0)



    def save(self, *args, **kwargs):
        self.tipo_de_produto = 'MANTIMENTO'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Mantimento'
        verbose_name_plural = 'Mantimentos'
        ordering = ['validade']

    def __str__(self):
        return super().__str__()  # Correção aqui
