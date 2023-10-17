
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from home.views import *

router = DefaultRouter()

router.register('FileShareView',FileShareView,basename='FileShareView')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
