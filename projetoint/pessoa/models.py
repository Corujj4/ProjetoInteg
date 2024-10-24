from django.db import models
from django.db.models.functions import Upper

from stdimage import StdImageField


class Pessoa(models.Model):
    nome = models.CharField("nome",max_length=50,help_text="Nome Completo")
    fone = models.CharField("fone",max_length=15,help_text="Numero de Telefone")
    email = models.EmailField("E-mail",max_length=100,help_text="Endereço de E-mail",unique=True)
    foto = StdImageField("Foto",upload_to='pessoas',delete_orphans=True, null=True,blank=True)
    idade = models.IntegerField("Idade", help_text="Idade")

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

