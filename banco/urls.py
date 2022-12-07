from xml.dom.minidom import Document
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from banco.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

