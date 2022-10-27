from django.db import models
from django_resized import ResizedImageField


class SliderHome(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.TextField('Descricao')
    ativo = models.BooleanField('Ativo', default=True)
    imagem = ResizedImageField(
        size=[1920, 1076],
        quality=100,
        upload_to='uploads/slider/%Y/%m/%d',

    )

    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return self.titulo


class ServicosHome(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.TextField('Descricao')
    ativo = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return self.titulo


class ServicosHomeItens(models.Model):
    servico = models.CharField('Serviço', max_length=150)
    servico_home = models.ForeignKey(ServicosHome, on_delete=models.CASCADE, verbose_name="Oferta")
    ativo = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return self.servico


class QuemSomos(models.Model):
    descricao = models.CharField('Quem Somos', max_length=150)

    def __str__(self):
        return self.descricao


class FrasesRandomicasHome(ServicosHome):
    pass


class RedesSociais(models.Model):
    nome = models.CharField('Nome', max_length=30)
    link = models.URLField('Link')
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    endereco = models.CharField('Endereço', max_length=150)
    telefone = models.CharField('Telefone', max_length=35)
    email = models.EmailField('E-mail')

    def __str__(self):
        return f"{self.endereco[1:15]}, {self.telefone},{self.telefone}"
