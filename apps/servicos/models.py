from django.db import models
from django.conf import settings
from django.db.models import signals
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
from .signals import create_slug_not_id, create_slug
from apps.users.models import User


class Categorias(models.Model):
    nome = models.CharField("Categoria", max_length=35, unique=True)
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'

    def __str__(self):
        return self.nome


class Servicos(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    nome = models.CharField("Nome", max_length=100)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, verbose_name="Categoria")
    descricao = RichTextField()
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'

    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    imagem = ResizedImageField(size=[500, 300], upload_to='uploads/servicos/%Y/%m/%d')

    def __str__(self):
        return self.nome


signals.post_save.connect(create_slug_not_id, sender=Servicos)
signals.post_save.connect(create_slug, sender=Categorias)