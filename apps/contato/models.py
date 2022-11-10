from django.db import models


class Contato(models.Model):
    contato = models.CharField('Contato', max_length=100)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=30)
    assunto = models.CharField('Assunto', max_length=100)
    mensagem = models.TextField('Mensagem')
    created_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.contato}"
