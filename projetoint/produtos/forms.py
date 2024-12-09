from django.forms import ModelForm

from .models import Remedio, Roupa, Mantimento


class RemedioModelForm(ModelForm):
    class Meta:
        model = Remedio
        fields = ['nome', 'quantidade', 'descricao', 'validade','gramatura']

        error_messages = {
            'nome' : {'required' : 'O nome do mantimento é um campo obrigatorio'},
            'quantidade' : {'required' : 'A quantidade do remedio é um campo obrigatoria'},
            'descricao' : {'required' : 'A descricao do remedio é obrigatoria'},


            'validade' : {'required' : 'A validade do remedio é obrigatoria'},
            'gramatura': {'required': 'A gramatura do remedio é obrigatoria'},


        }

class RoupaModelForm(ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome', 'quantidade', 'descricao', 'genero', 'tamanho']

        error_messages = {
            'nome' : {'required' : 'O nome da roupa é um campo obrigatorio'},
            'quantidade' : {'required' : 'A quantidade de roupas é um campo obrigatorio'},
            'descricao' : {'required' : 'A descricao da roupa é obrigatoria'},


            'genero' : {'required' : 'O tamanho da roupa é obrigatorio'},
            'tamanho' : {'required' : 'O genero da roupa é obrigatorio'},


        }

class MantimentoModelForm(ModelForm):
    class Meta:
        model = Mantimento
        fields = ['nome', 'quantidade', 'descricao', 'validade', 'categoria']

        error_messages = {
            'nome' : {'required' : 'O nome do mantimento é um campo obrigatorio'},
            'quantidade' : {'required' : 'A quantidade do mantimento é um campo obrigatoria'},
            'descricao' : {'required' : 'A descricao do mantimento é obrigatoria'},


            'validade' : {'required' : 'A validade do mantimento é obrigatoria'},
            'categoria' : {'required' : 'A categoria do mantimento é obrigatoria'},





        }