from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SliderHome, ServicosHome, FrasesRandomicasHome


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = SliderHome.objects.filter(ativo=True)
        context['about'] = ServicosHome.objects.get(titulo="O QUE OFERECEMOS", ativo=True)
        context['frases'] = FrasesRandomicasHome.objects.order_by('?').first()
        return context
