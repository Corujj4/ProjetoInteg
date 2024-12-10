from django.forms import ModelForm, inlineformset_factory

from lista.models import Lista
from listaprodutos.models import ListaProdutos


class ListaModelForm(ModelForm):
    class Meta:
        model = Lista
        fields = ['nome']

        error_messages = {
            'nome' : {'required' : 'O nome do mantimento é um campo obrigatorio'},


        }
ListaProdutosInline = inlineformset_factory(Lista, ListaProdutos,fk_name='lista',fields=('produto','quantidade'),extra=1,can_delete=True )