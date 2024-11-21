from .views import ChamadoView, ChamadoAddView, ChamadoUpdateView, ChamadoDeleteView
from django.urls import path

urlpatterns = [
    path('chamados',ChamadoView.as_view(),name='chamado'),
    path('chamado/adicionar/', ChamadoAddView.as_view(), name='chamado_adicionar'),
    path('<int:pk>/chamado/editar/', ChamadoUpdateView.as_view(), name='chamado_editar'),
    path('<int:pk>/chamado/apagar/', ChamadoDeleteView.as_view(), name='chamado_apagar'),


]