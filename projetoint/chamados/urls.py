from .views import ChamadoView, ChamadoAddView
from django.urls import path

urlpatterns = [
    path('chamados',ChamadoView.as_view(),name='chamado'),
    path('chamado/adicionar/', ChamadoAddView.as_view(), name='chamado_adicionar'),


]