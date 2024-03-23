from django.conf import settings
from django.urls import path
from Main import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("upload_files/", views.upload_files, name="upload_files"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
