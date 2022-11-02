from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.db.models import Q
from .models import SliderHome, ServicosHome, FrasesRandomicasHome
from apps.servicos.models import Servicos
from .forms import ServicosSearchForm


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = SliderHome.objects.filter(ativo=True)
        context['about'] = ServicosHome.objects.get(titulo="O QUE OFERECEMOS", ativo=True)
        context['frases'] = FrasesRandomicasHome.objects.order_by('?').first()
        context['servicos'] = Servicos.objects.order_by('?').all()[:3]
        return context


class TodosOsServicos(ListView):
    model = Servicos
    template_name = 'home/servicos_home.html'

    def get_queryset(self, **kwargs):
        servico = self.request.GET.get('nome', '')

        return Servicos.objects.filter(Q(nome__contains=servico) | Q(categoria__nome__icontains=servico))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TodosOsServicos, self).get_context_data(**kwargs)
        context['busca'] = ServicosSearchForm()

        return context


class ServicoDetalhe(DetailView):
    model = Servicos
    template_name = 'home/servico_detalhe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicos'] = Servicos.objects.order_by('?').all()[:3]
        return context
