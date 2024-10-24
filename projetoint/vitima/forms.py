
from django.forms import ModelForm

from vitima.models import Vitima


class VitimaModelForm(ModelForm):
    class Meta:
        model = Vitima
        fields = ['nome', 'fone', 'email', 'foto', 'necessidade',]

        error_messages = {
            'none' : {'required' : 'O nome do funcionario é um campo obrigatorio'},
            'fone' : {'required' : 'O telefone do funcionario é um campo obrigatorio'},
            'email' : {'required' : 'O nome do funcionario é um campo obrigatorio',
                       'invalid' : 'Formato invalido para o e-mail. Exemplo de formatado valido: fulano@dominio.com',
                       'unique' : 'Email ja cadastrado'
                       },
            'necessidade': {'required' : 'A necessidade é um campo obrigatorio'},
        }