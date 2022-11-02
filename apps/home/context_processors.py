from apps.servicos.models import Categorias
from .models import RedesSociais, Contato


def contato(request):
    return {
        "site_infor": Contato.objects.first()
    }


def servicos_categorias(request):
    return {
        "categorias": Categorias.objects.all()
    }


def social(request):
    return {
        "social": RedesSociais.objects.all()
    }