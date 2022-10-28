from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Servicos


class ServicosAdminForm(forms.ModelForm):
    descricao = forms.CharField(widget=CKEditorWidget())
    author = forms.HiddenInput()

    class Meta:
        model = Servicos
        fields = "__all__"
