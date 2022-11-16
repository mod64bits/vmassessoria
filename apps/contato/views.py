from django.http import HttpResponseRedirect
from .forms import ContatoForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Contato
from apps.core.send_email import SendVmMail


class ContatoView(SuccessMessageMixin, CreateView):
    template_name = 'contato/contato.html'
    form_class = ContatoForm
    model = Contato
    success_url = '/contato/'
    success_message = "Sua menssagem foi recebida com sucesso!"



    def form_valid(self, form):
        """If the form is valid, send an email and then save the form."""
        print()
        MailSend = SendVmMail(
            subject=form.data['assunto'],
            nome=form.data['contato'], assunto=form.data['assunto'],
            telefone=form.data['telefone'],
            mensagem=form.data['mensagem']
        )
        MailSend.contato(email=form.data['email'])
        messages.add_message(
            self.request, messages.SUCCESS, self.success_message
        )
        return HttpResponseRedirect('/contato/')
    def form_invalid(self, form):
        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(self.request, 'Você deve passar no teste reCAPTCH')
                continue
            messages.error(self.request, error)

        return HttpResponseRedirect('/contato/')