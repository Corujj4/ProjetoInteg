from django.forms import ModelForm

from pessoa.models import Pessoa


class PessoaModelForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'endereco', 'fone', 'email', 'foto', 'idade']

        error_messages = {
            'none' : {'required' : 'O nome do cliente é um campo obrigatorio'},
            'endereco' : {'required' : 'O endereço do cliente é um campo obrigatorio'},
            'fone' : {'required' : 'O telefone do cliente é um campo obrigatorio'},
            'email' : {'required' : 'O nome do cliente é um campo obrigatorio',
                       'invalid' : 'Formato invalido para o e-mail. Exemplo de formatado valido: fulano@dominio.com',
                       'unique' : 'Email ja cadastrado'},
                       'idade' : {'required' : 'A idade da pessoa é um campo obrigatorio'},

        }