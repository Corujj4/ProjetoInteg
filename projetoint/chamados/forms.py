from django.forms import ModelForm

from .models import Chamado


class ChamadoModelForm(ModelForm):
    class Meta:
        model = Chamado
        fields = '__all__'

        error_messages = {

            'quantidade' : {'required' : 'A quantidade de items é um campo obrigatorio'},
            'descricao' : {'required' : 'A descricao do chamado é obrigatorio'},
            'unidade': {'required': 'A unidade de items ( caso houver ) é obrigatorio'},
            'situacao': {'required': 'A descricao de situacao do chamado é '},








        }