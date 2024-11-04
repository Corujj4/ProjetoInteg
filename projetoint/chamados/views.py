from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib import messages

from chamados.forms import ChamadoModelForm
from chamados.models import Chamado


class ChamadoView(ListView):
    model = Chamado
    template_name = 'chamados.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs =  super(ChamadoView,self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem

        else:
            return messages.info(self.request,'Nao existem funcionarios cadastrados.')


class ChamadoAddView(SuccessMessageMixin,CreateView):
    model = Chamado
    form_class = ChamadoModelForm
    template_name = 'Chamado_form.html'
    success_url = reverse_lazy('chamado')
    success_message = 'Chamado cadastrado com sucesso!'



