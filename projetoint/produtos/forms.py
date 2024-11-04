from django.forms import ModelForm

from .models import Remedio, Roupa, Mantimento


class RemedioModelForm(ModelForm):
    class Meta:
        model = Remedio
        fields = '__all__'

        error_messages = {
            'nome' : {'required' : 'O nome do mantimento é um campo obrigatorio'},
            'quantidade' : {'required' : 'A quantidade do mantimento é um campo obrigatoria'},
            'descricao' : {'required' : 'A descricao do mantimento é obrigatoria'},


            'validade' : {'required' : 'A validade do remedio é obrigatoria'},






        }

class RoupaModelForm(ModelForm):
    class Meta:
        model = Roupa
        fields = '__all__'

        error_messages = {
            'nome' : {'required' : 'O nome do mantimento é um campo obrigatorio'},
            'quantidade' : {'required' : 'A quantidade do mantimento é um campo obrigatoria'},
            'descricao' : {'required' : 'A descricao do mantimento é obrigatoria'},


            'genero' : {'required' : 'O tamanho da roupa é obrigatorio'},
            'tamanho' : {'required' : 'O genero da roupa é obrigatorio'},





        }

class MantimentoModelForm(ModelForm):
    class Meta:
        model = Mantimento
        fields = '__all__'

        error_messages = {
            'nome' : {'required' : 'O nome do mantimento é um campo obrigatorio'},
            'quantidade' : {'required' : 'A quantidade do mantimento é um campo obrigatoria'},
            'descricao' : {'required' : 'A descricao do mantimento é obrigatoria'},


            'validade' : {'required' : 'A validade do mantimento é obrigatoria'},
            'categoria' : {'required' : 'A categoria do mantimento é obrigatoria'},





        }