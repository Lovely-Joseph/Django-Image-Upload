from django.urls import path
from gallery_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('imgupload/',views.ImgUpload,name='imgupload'),
]
