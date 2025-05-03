from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin, View
from lista.forms import ListaModelForm, ListaProdutosInline
from lista.models import Lista
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.
class ListaView(PermissionRequiredMixin,ListView):
    permission_required = 'lista.view_lista'
    permission_denied_message = 'Visualizar Lista'
    model = Lista
    template_name = 'listas.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs =  super(ListaView,self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem

        else:
            return messages.info(self.request,'Nao existem Lista cadastradas.')

class ListaAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'lista.view_lista'
    permission_denied_message = 'Visualizar Lista'
    model = Lista
    form_class = ListaModelForm
    template_name = 'lista_form.html'
    success_url = reverse_lazy('listas')
    success_message = 'Lista cadastrada com sucesso!'

class ListaUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'lista.update_lista'
    permission_denied_message = 'Editar Lista'
    model = Lista
    form_class = ListaModelForm
    template_name = 'lista_form.html'
    success_url = reverse_lazy('listas')
    success_message = 'Lista alterada com sucesso!'

class ListaDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'lista.delete_lista'
    permission_denied_message = 'Deletar Lista'
    model = Lista
    template_name = 'lista_apagar.html'
    success_url = reverse_lazy('listas')
    success_message = 'Lista cadastrada com sucesso!'

class ListaInlineEditView(TemplateResponseMixin,View):
    template_name = 'lista_form_inline.html'

    def get_formset(self, data=None):
        return ListaProdutosInline(instance=self.lista, data=data)

    def dispatch(self, request, pk):
        self.lista = get_object_or_404(Lista, id=pk)
        return super().dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'Lista':self.lista, 'formset':formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('listas')
        return self.render_to_response({'Lista':self.lista, 'formset':formset})
