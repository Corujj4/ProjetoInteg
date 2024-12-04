from django.forms import ModelForm

from .models import Chamado


class ChamadoModelForm(ModelForm):
    class Meta:
        model = Chamado
        fields = ['unidade','produto','funcionario','vitima','prioridade', 'descricao']

        error_messages = {

           'produto' : {'required': 'O produto é obrigatorio'},
            'unidade': {'required': 'A unidade de items ( caso houver ) é obrigatorio'},
            'funcionario' : {'required': 'O funcionario é obrigatorio'},
            'vitima' : {'required' : 'A vitima é obrigatoria'},
            'prioridade' : {'required' : 'A prioridade é obrigatoria'},
            'descricao' : {'required' : 'A descricao é obrigatoria'},

        }

