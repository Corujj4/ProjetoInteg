
from django.forms import ModelForm

from funcionario.models import Funcionario


class FuncionarioModelForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'fone', 'email','funcao', 'foto', 'hrs', 'idade']

        error_messages = {
            'none' : {'required' : 'O nome do funcionario é um campo obrigatorio'},
            'fone' : {'required' : 'O telefone do funcionario é um campo obrigatorio'},
            'funcao': {'required': 'A função do funcionario é um campo obrigatorio'},
            'email' : {'required' : 'O nome do funcionario é um campo obrigatorio',
                       'invalid' : 'Formato invalido para o e-mail. Exemplo de formatado valido: fulano@dominio.com',
                       'unique' : 'Email ja cadastrado'
                       },
            'idade': {'required': 'A idade da pessoa é um campo obrigatorio'},
            'hrs': {'required' : 'Horas Totais de trabalho é um campo obrigatorio'},
        }