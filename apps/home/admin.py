from django.contrib import admin
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


@admin.register(FrasesRandomicasHome)
class FrasesRandomicasHomeAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Serviço home", {"fields": ("titulo", "descricao", "ativo")}),
    )


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Contato", {"fields": ("endereco", "telefone", "email")}),
    )


@admin.register(RedesSociais)
class RedesSociaisAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Redes Sociais", {"fields": ("nome", "link")}),
    )