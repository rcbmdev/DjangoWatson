from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from recognition import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recognition/', include('recognition.urls')),
    path('nlu_understanding/', include('nlu_understanding.urls')),
    path('translator/', include('translator.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
