from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.home import urls as home_urls
from apps.contato.views import ContatoView


urlpatterns = [
    path("contato/", ContatoView.as_view(), name="contato"),
    path("", include(home_urls)),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
