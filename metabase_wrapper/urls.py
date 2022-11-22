from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main_view'),
    path('upload/', file_upload, name='file_upload'),
    path('upload_start/', UploadStartView.as_view(), name='upload_start')
]