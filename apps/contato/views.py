from django.shortcuts import render
from .forms import ContatoForm
from django.views.generic.edit import FormView


class ContatoView(FormView):
    template_name = 'contato/contato.html'
    form_class = ContatoForm
    success_url = '/thanks/'
