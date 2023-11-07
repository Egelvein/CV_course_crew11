from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main_camera, name='main'),
    path('results/<chip_id>', views.result, name='result'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

