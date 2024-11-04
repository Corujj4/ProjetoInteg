from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from .forms import RemedioModelForm, RoupaModelForm, MantimentoModelForm
from .models import Remedio, Roupa, Mantimento, Produtos
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.

class ProdutoView(ListView):
    model = Produtos
    template_name = 'produtos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs =  super(ProdutoView,self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem

        else:
            return messages.info(self.request,'Nao existem clientes cadastrados.')

class RemedioAddView(SuccessMessageMixin,CreateView):
    model = Remedio
    form_class = RemedioModelForm
    template_name = 'remedio_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Remedio cadastrado com sucesso!'

class RemedioUpdateView(SuccessMessageMixin,UpdateView):
    model = Remedio
    form_class = RemedioModelForm
    template_name = 'remedio_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Remedio alterado com sucesso!'

class RemedioDeleteView(SuccessMessageMixin,DeleteView):
    model = Remedio
    template_name = 'remedio_apagar.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Remedio cadastrado com sucesso!'


class RoupaAddView(SuccessMessageMixin,CreateView):
    model = Roupa
    form_class = RoupaModelForm
    template_name = 'roupa_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Roupa cadastrada com sucesso!'

class RoupaUpdateView(SuccessMessageMixin,UpdateView):
    model = Roupa
    form_class = RoupaModelForm
    template_name = 'roupa_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Roupa alterado com sucesso!'

class RoupaDeleteView(SuccessMessageMixin,DeleteView):
    model = Roupa
    template_name = 'roupa_apagar.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Roupa cadastrado com sucesso!'


class MantimentoAddView(SuccessMessageMixin,CreateView):
    model = Mantimento
    form_class = MantimentoModelForm
    template_name = 'mantimentos_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Mantimento cadastrado com sucesso!'

class MantimentoUpdateView(SuccessMessageMixin,UpdateView):
    model = Mantimento
    form_class = MantimentoModelForm
    template_name = 'mantimento_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Mantimento alterado com sucesso!'

class MantimentoDeleteView(SuccessMessageMixin,DeleteView):
    model = Mantimento
    template_name = 'mantimento_apagar.html'
    success_url = reverse_lazy('produtos')
    success_message = 'mantimento cadastrado com sucesso!'