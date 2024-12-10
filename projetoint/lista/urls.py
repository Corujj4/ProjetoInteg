from .views import ListaView, ListaAddView, ListaUpdateView, ListaDeleteView, ListaInlineEditView
from django.urls import path

urlpatterns = [
    path('lista/',ListaView.as_view(),name='listas'),
    path('lista/adicionar/',ListaAddView.as_view(),name='lista_adicionar'),
    path('<int:pk>/lista/editar/',ListaUpdateView.as_view(),name='lista_editar'),
    path('<int:pk>/lista/apagar/',ListaDeleteView.as_view(), name='lista_apagar'),
    path('<int:pk>/lista/inline/',ListaInlineEditView.as_view(), name='lista_inline'),

]