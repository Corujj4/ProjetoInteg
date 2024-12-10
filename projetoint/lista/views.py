from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin, View
from lista.forms import ListaModelForm, ListaProdutosInline
from lista.models import Lista
from django.contrib import messages


# Create your views here.
class ListaView(ListView):
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

class ListaAddView(SuccessMessageMixin,CreateView):
    model = Lista
    form_class = ListaModelForm
    template_name = 'lista_form.html'
    success_url = reverse_lazy('listas')
    success_message = 'Lista cadastrada com sucesso!'

class ListaUpdateView(SuccessMessageMixin,UpdateView):
    model = Lista
    form_class = ListaModelForm
    template_name = 'lista_form.html'
    success_url = reverse_lazy('listas')
    success_message = 'Lista alterada com sucesso!'

class ListaDeleteView(SuccessMessageMixin,DeleteView):
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
