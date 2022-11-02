from django.forms import ModelForm
from django import forms
from apps.servicos.models import Servicos


class ServicosSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServicosSearchForm, self).__init__(*args, **kwargs)
        self.fields['nome'] = forms.CharField(max_length=20, required=False)
        #self.fields['categoria'] = forms.ChoiceField(required=False)

    class Meta:
        model = Servicos
        fields = ['nome']
