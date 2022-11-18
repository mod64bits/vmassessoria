from django.db import models
from apps.core.signals import create_slug
from django.db.models import signals


class TipoCliente(models.Model):
    tipo = models.CharField('Tipo', max_length=50)
    created_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name_plural = 'Tipos de Clientes'
        verbose_name = 'Tipo de Cliente'


class Cliente(models.Model):
    tipo = models.ForeignKey(TipoCliente, on_delete=models.CASCADE, verbose_name='Tipo de Cliente')
    nome = models.CharField('Nome', max_length=150)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=30)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=30)
    endereco = models.CharField('Endereço', max_length=200)
    bairro = models.CharField('Bairro', max_length=50)
    referencia = models.CharField('Referencia', max_length=100)

    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'

    slug_from = 'nome'

    def __str__(self):
        return f"{self.nome}-{self.cpf_cnpj}"

    class Meta:
        verbose_name_plural = 'Clientes'
        verbose_name = 'Cliente'


signals.post_save.connect(create_slug, sender=Cliente)