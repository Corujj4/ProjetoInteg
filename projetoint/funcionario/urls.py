from .views import FuncionariosView, FuncionarioAddView, FuncionarioDeleteView, FuncionarioUpdateView
from django.urls import path

urlpatterns = [
    path('funcionario',FuncionariosView.as_view(),name='funcionarios'),
    path('funcionario/adicionar/',FuncionarioAddView.as_view(),name='funcionario_adicionar'),
    path('<int:pk>/funcionario/editar/',FuncionarioUpdateView.as_view(),name='funcionario_editar'),
    path('<int:pk>/funcionario/apagar/',FuncionarioDeleteView.as_view(), name='funcionario_apagar'),

]