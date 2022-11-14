from django.http import HttpResponseRedirect

from .forms import ContatoForm
from django.views.generic.edit import CreateView
from .models import Contato
from apps.core.send_email import SendVmMail
import requests

class ContatoView(CreateView):
    template_name = 'contato/contato.html'
    form_class = ContatoForm
    model = Contato
    success_url = '/contato/'


    def form_valid(self, form):
        """If the form is valid, send an email and then save the form."""
        print()
        MailSend = SendVmMail(subject="test", nome="test", assunto="tesdt" ,telefone="199996647569", mensagem="mensagem")
        MailSend.contato(email="marciooliveiradedeus@gmail.com")
        return HttpResponseRedirect('/contato/')