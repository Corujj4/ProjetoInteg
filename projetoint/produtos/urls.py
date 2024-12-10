from .views import RemedioDeleteView, RemedioUpdateView, RemedioAddView, RoupaUpdateView, RoupaAddView, RoupaDeleteView, \
    MantimentoAddView, MantimentoUpdateView, MantimentoDeleteView, ProdutoView
from django.urls import path


urlpatterns = [

    path('produtos', ProdutoView.as_view(), name='produtos'),

    path('remedio/adicionar/',RemedioAddView.as_view(),name='remedio_adicionar'),
    path('<int:pk>/remedio/editar/',RemedioUpdateView.as_view(),name='remedio_editar'),
    path('<int:pk>/remedio/apagar/',RemedioDeleteView.as_view(), name='remedio_apagar'),

    path('roupa/adicionar/', RoupaAddView.as_view(), name='roupa_adicionar'),
    path('<int:pk>/roupa/editar/', RoupaUpdateView.as_view(), name='roupa_editar'),
    path('<int:pk>/roupa/apagar/', RoupaDeleteView.as_view(), name='roupa_apagar'),

    path('mantimento/adicionar/',MantimentoAddView.as_view(),name='mantimento_adicionar'),
    path('<int:pk>/mantimento/editar/',MantimentoUpdateView.as_view(),name='mantimento_editar'),
    path('<int:pk>/mantimento/apagar/',MantimentoDeleteView.as_view(), name='mantimento_apagar'),


]

