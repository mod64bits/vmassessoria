from django import forms
from .models import Contato
from apps.core.send_email import SendVmMail


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'



