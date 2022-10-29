from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import SliderHome, ServicosHome, FrasesRandomicasHome
from apps.servicos.models import Servicos


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
    context_object_name = 'servicos'
    template_name = 'home/servicos_home.html'
