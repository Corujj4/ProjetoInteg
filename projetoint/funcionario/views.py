
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from funcionario.forms import FuncionarioModelForm
from funcionario.models import Funcionario
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin



# Create your views here.
class FuncionariosView(PermissionRequiredMixin,ListView):
    permission_required = 'funcionario.view_funcionario'
    permission_denied_message = 'Visualizar funcionario'
    model = Funcionario
    template_name = 'funcionarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs =  super(FuncionariosView,self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem

        else:
            return messages.info(self.request,'Nao existem funcionarios cadastrados.')

class FuncionarioAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'funcionario.add_funcionario'
    permission_denied_message = 'Cadastrar funcionario'
    model = Funcionario
    form_class = FuncionarioModelForm
    template_name = 'Funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionario cadastrado com sucesso!'

class FuncionarioUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'funcionario.update_funcionario'
    permission_denied_message = 'Editar funcionario'
    model = Funcionario
    form_class = FuncionarioModelForm
    template_name = 'Funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionario alterado com sucesso!'

class FuncionarioDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'funcionario.delete_funcionario'
    permission_denied_message = 'Deletar funcionario'
    model = Funcionario
    template_name = 'funcionario_apagar.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionario cadastrado com sucesso!'