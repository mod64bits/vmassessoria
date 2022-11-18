from django.contrib import admin
from .models import TipoCliente, Cliente


@admin.register(TipoCliente)
class TipoClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Tipo de Cliente", {"fields": ("tipo",)}),
    )


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Cliente", {"fields": ("tipo", "nome", "cpf_cnpj", "email", "telefone", "endereco", "bairro", "referencia",)}),
    )