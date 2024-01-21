from django.urls import  path
from Main import views
urlpatterns=[
    path("",views.index,name="index"),
    path("upload_files/",views.upload_files,name="upload_files")
]