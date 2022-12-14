from django.urls import path, re_path
from .views import HomeView
from apps.home.views import TodosOsServicos, ServicoDetalhe
app_name = 'home'

urlpatterns = [
    path('servico/<slug:slug>/', ServicoDetalhe.as_view(), name='servicos_detalhe'),
    path('servicos/', TodosOsServicos.as_view(), name='servicos_home'),
    path('', HomeView.as_view(), name='home'),
]