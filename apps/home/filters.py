import django_filters
from apps.servicos.models import Categorias, Servicos


class ServicosFilter(django_filters.FilterSet):

    class Meta:
        model = Servicos
        fields = {}







