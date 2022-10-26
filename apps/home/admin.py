from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import ServicosHome, SliderHome, FrasesRandomicasHome, Contato, QuemSomos, RedesSociais, ServicosHomeItens


@admin.register(SliderHome)
class SliderHomeAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Slides", {"fields": ("titulo", "descricao", "ativo", "imagem")}),
    )

    jazzmin_section_order = ("titulo", "ativo", "created_at")
    list_filter = ("titulo",)
    filter_input_length = {
        "title": 5,
    }


class ServicosHomeInline(admin.StackedInline):
    model = ServicosHomeItens
    extra = 0


@admin.register(ServicosHome)
class OQueOferecemosAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Serviço home", {"fields": ("titulo", "descricao", "ativo")}),
    )
    inlines = [
        ServicosHomeInline,
    ]


@admin.register(ServicosHomeItens)
class ServicosHomeAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Serviços Home", {"fields": ("servico", "servico_orerecido", "ativo")}),
    )

