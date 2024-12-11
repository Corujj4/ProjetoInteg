
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from vitima.forms import VitimaModelForm
from vitima.models import Vitima
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin



# Create your views here.
class VitimasView(PermissionRequiredMixin,ListView):
    permission_required = 'vitima.view_vitima'
    permission_denied_message = 'Visualizar vitima'
    model = Vitima
    template_name = 'vitimas.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs =  super(VitimasView,self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem

        else:
            return messages.info(self.request,'Nao existem vitimas cadastrados.')

class VitimaAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'vitima.add_vitima'
    permission_denied_message = 'Adicionar vitima'
    model = Vitima
    form_class = VitimaModelForm
    template_name = 'vitima_form.html'
    success_url = reverse_lazy('vitimas')
    success_message = 'Vitima cadastrado com sucesso!'

class VitimaUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'vitima.update_vitima'
    permission_denied_message = 'Editar vitima'
    model = Vitima
    form_class = VitimaModelForm
    template_name = 'vitima_form.html'
    success_url = reverse_lazy('vitimas')
    success_message = 'Vitima alterado com sucesso!'

class VitimaDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'vitima.delete_vitima'
    permission_denied_message = 'Deletar vitima'
    model = Vitima
    template_name = 'vitima_apagar.html'
    success_url = reverse_lazy('vitimas')
    success_message = 'Vitima cadastrado com sucesso!'