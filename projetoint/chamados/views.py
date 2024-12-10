from django.shortcuts import reverse

from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.views.generic.base import TemplateResponseMixin, View

import produtos.views
from chamados.forms import ChamadoModelForm
from chamados.models import Chamado
from produtos.views import RoupaDeleteView


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
            return messages.info(self.request,'Nao existem chamados cadastrados.')


class ChamadoAddView(SuccessMessageMixin,CreateView):
    model = Chamado
    form_class = ChamadoModelForm
    template_name = 'chamado_form.html'
    success_url = reverse_lazy('chamado')
    success_message = 'Chamado cadastrado com sucesso!'

    def form_valid(self, form):
        chamado = form.save()
        '''self.enviar_emailinicio(chamado)'''
        return super().form_valid(form)

    def enviar_emailinicio(self, chamado):
        email = []
        email.append(chamado.funcionario.email)
        email.append(chamado.vitima.email)
        dados = {
            'funcionario': chamado.funcionario.nome,
            'vitima': chamado.vitima.nome,
            'produto': chamado.produto.nome,
            'quantidade': chamado.unidade,
            'descricao': chamado.descricao,
        }

        texto_email = render_to_string('emails/texto_abertoemail.txt', dados)
        html_email = render_to_string('emails/texto_abertoemail.html', dados)

        send_mail(
            subject='Ajudantos',
            message=texto_email,
            from_email='raphaelsiqueiradesouza@gmail.com',
            recipient_list=email,
            html_message=html_email,
            fail_silently=False,
        )


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


    def enviar_email(self, chamado):

        email =[]
        email.append(chamado.funcionario.email)
        email.append(chamado.vitima.email)
        dados = {
            'funcionario': chamado.funcionario.nome,
            'vitima': chamado.vitima.nome,
            'produto':chamado.produto.nome,
            'quantidade': chamado.unidade,
            'descricao' : chamado.descricao,
            }


        texto_email = render_to_string('emails/texto_fechadoemail.txt', dados)
        html_email = render_to_string('emails/texto_fechadoemail.html', dados)


        send_mail(
            subject='Ajudantos',
            message=texto_email,
            from_email='raphaelsiqueiradesouza@gmail.com',
            recipient_list=email,
            html_message=html_email,
            fail_silently=False,
        )

        return redirect('chamado')

    def get_object(self, queryset=None):
        chamado = get_object_or_404(Chamado, pk=self.kwargs['pk'])

        if chamado.status == 'Em andamento':
            try:
                # Verifica se o produto relacionado ao chamado ainda existe
                produto = chamado.produto
                chamado.status = 'Finalizado'
                chamado.save()
                produto.delete()
                return chamado
            except chamado.produto.__class__.DoesNotExist:
                # Produto não existe, exibe mensagem e mantém o chamado aberto
                messages.error(self.request, "O produto relacionado a este chamado está indisponível no estoque.")
                return chamado

            # Caso o produto exista, conclui o chamado


            self.enviar_email(chamado)
            messages.success(self.request, "Chamado finalizado com sucesso!")
        else:
            messages.info(self.request, "Este chamado já foi finalizado.")

        return chamado