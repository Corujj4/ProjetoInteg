from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import RemedioModelForm, RoupaModelForm, MantimentoModelForm
from .models import Remedio, Roupa, Mantimento, Produtos
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class ProdutoView(PermissionRequiredMixin,ListView):
    permission_required = 'produto.view_produto'
    permission_denied_message = 'Visualizar produto'
    model = Produtos
    template_name = 'produtos.html'


    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs =  super(ProdutoView,self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 15)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem

        else:
            return messages.info(self.request,'Nao existem clientes cadastrados.')

class RemedioAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'remedio.add_remedio'
    permission_denied_message = 'Adicionar remedio'
    model = Remedio
    form_class = RemedioModelForm
    template_name = 'remedio_form.html'
    success_url = reverse_lazy('listas')
    success_message = 'Remedio cadastrado com sucesso!'

class RemedioUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'remedio.update_remedio'
    permission_denied_message = 'Editar remedio'
    model = Remedio
    form_class = RemedioModelForm
    template_name = 'remedio_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Remedio alterado com sucesso!'

class RemedioDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'remedio.delete_remedio'
    permission_denied_message = 'Deletar remedio'
    model = Remedio
    template_name = 'remedio_apagar.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Remedio cadastrado com sucesso!'


class RoupaAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'roupa.add_produto'
    permission_denied_message = 'Cadastrar roupa'
    model = Roupa
    form_class = RoupaModelForm
    template_name = 'roupa_form.html'
    success_url = reverse_lazy('listas')
    success_message = 'Roupa cadastrada com sucesso!'

class RoupaUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'roupa.update_produto'
    permission_denied_message = 'Editar roupa'
    model = Roupa
    form_class = RoupaModelForm
    template_name = 'roupa_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Roupa alterado com sucesso!'

class RoupaDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'roupa.delete_produto'
    permission_denied_message = 'Deletar roupa'
    model = Roupa
    template_name = 'roupa_apagar.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Roupa cadastrado com sucesso!'


class MantimentoAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'mantimento.add_mantimento'
    permission_denied_message = 'Adicionar mantimento'
    model = Mantimento
    form_class = MantimentoModelForm
    template_name = 'mantimentos_form.html'
    success_url = reverse_lazy('listas')
    success_message = 'Mantimento cadastrado com sucesso!'

class MantimentoUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'mantimento.update_mantimento'
    permission_denied_message = 'Editar mantimento'
    model = Mantimento
    form_class = MantimentoModelForm
    template_name = 'mantimentos_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Mantimento alterado com sucesso!'

class MantimentoDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'mantimento.delete_mantimento'
    permission_denied_message = 'Deletar mantimento '
    model = Mantimento
    template_name = 'mantimento_apagar.html'
    success_url = reverse_lazy('produtos')
    success_message = 'mantimento cadastrado com sucesso!'





