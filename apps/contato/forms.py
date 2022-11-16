from django import forms
from .models import Contato
from apps.core.send_email import SendVmMail
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContatoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        self.fields['captcha'] = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    class Meta:
        model = Contato
        fields = '__all__'



