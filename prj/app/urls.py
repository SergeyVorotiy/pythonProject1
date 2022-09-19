from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import FileModelView, clear


urlpatterns = [
    path('', FileModelView.as_view(), name='mian'),
    path('clear', clear)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
