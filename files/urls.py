# files/urls.py
from django.urls import path
from .views import file_list_view, file_upload_view, file_delete_view

urlpatterns = [
    path('', file_list_view, name='file_list'),
    path('upload/', file_upload_view, name='upload_file'),
    path('delete/<int:pk>/', file_delete_view, name='delete_file'),
]
