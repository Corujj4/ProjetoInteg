from .views import ChamadoView, ChamadoAddView, ChamadoUpdateView, ChamadoDeleteView, ChamadoExibir
from django.urls import path

urlpatterns = [
    path('chamado',ChamadoView.as_view(),name='chamado'),
    path('chamado/adicionar/', ChamadoAddView.as_view(), name='chamado_adicionar'),
    path('<int:pk>/chamado/editar/', ChamadoUpdateView.as_view(), name='chamado_editar'),
    path('<int:pk>/chamado/apagar/', ChamadoDeleteView.as_view(), name='chamado_apagar'),
    path('<int:pk>/chamado/exibir/', ChamadoExibir.as_view(), name='chamado_exibir'),


]