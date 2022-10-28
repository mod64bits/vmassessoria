from django.contrib import admin
from django.contrib.admin import display

from .models import Categorias, Servicos
from .forms import ServicosAdminForm


@admin.register(Categorias)
class RedesSociaisAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Categorias Serviços", {"fields": ("nome", )}),
    )


@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    form = ServicosAdminForm
    list_display = ("nome", "author", "created_at",)
    fieldsets = (
        ("Serviços", {"fields": ("nome", "categoria", "descricao", "imagem",)}),
    )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(ServicosAdmin, self).save_model(request, obj, form, change)
