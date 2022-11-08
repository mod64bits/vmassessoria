from django import forms


class ContatoForm(forms.Form):
    contato = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    telefone = forms.EmailField(label='Telefone')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass