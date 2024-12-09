from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.views.generic.base import TemplateResponseMixin, View
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
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem

        else:
            return messages.info(self.request,'Nao existem chamados cadastrados.')


class ChamadoAddView(SuccessMessageMixin,CreateView):
    model = Chamado
    form_class = ChamadoModelForm
    template_name = 'chamado_form.html'
    success_url = reverse_lazy('chamado')
    success_message = 'Chamado cadastrado com sucesso!'

class ChamadoDeleteView(SuccessMessageMixin,DeleteView):
    model = Chamado
    template_name = 'chamado_apagar.html'
    success_url = reverse_lazy('chamado')
    success_message = 'Chamado deletado com sucesso!'

class ChamadoUpdateView(SuccessMessageMixin,UpdateView):
    model = Chamado
    form_class = ChamadoModelForm
    template_name = 'chamado_form.html'
    success_url = reverse_lazy('chamado')
    success_message = 'Chamado editado com sucesso!'


class ChamadoExibir(DetailView):
    model = Chamado
    template_name = 'chamado_exibir.html'

    def get_object(self, queryset=None):
        chamado = get_object_or_404(Chamado, pk=self.kwargs['pk'])


        if chamado.status == 'Em andamento':
            chamado.status = 'Finalizado'
            chamado.save()
            '''
            # Envia um e-mail de notificação
            self.enviar_email(chamado)
            messages.success(self.request, "Chamado finalizado com sucesso!")
        else:
            messages.info(self.request, "Este chamado já foi finalizado.")
'''
        return chamado
'''
    def enviar_email(self, chamado):
        # Configura o destinatário e os dados do e-mail
        email = [chamado.cliente.email]  # Assumindo que o chamado tem um campo cliente com e-mail
        dados = {
            'cliente': chamado.cliente.nome,
            'descricao': chamado.descricao,
            'status': chamado.get_status_display(),  # Exibe a descrição do status
            'data_abertura': chamado.data_abertura,
            'data_fechamento': chamado.data_fechamento or 'Não definida',
        }

        # Gera o texto e o HTML do e-mail
        texto_email = render_to_string('emails/chamado_finalizado.txt', dados)
        html_email = render_to_string('emails/chamado_finalizado.html', dados)

        # Envia o e-mail
        send_mail(
            subject='Chamado Finalizado',
            message=texto_email,
            from_email='seuemail@example.com',
            recipient_list=email,
            html_message=html_email,
            fail_silently=False,
        )

    def post(self, request, *args, **kwargs):
        '''
