from django.urls import path

from . import views

urlpatterns = [
    path('files/view/<int:id>/', views.fileView, name='file-view'),
    path('files/newFile/', views.newFile, name='new-file'),
    path('files/edit/<int:id>', views.editFile, name='edit-file'),
    path('files/delete/<int:id>', views.deleteFile, name='delete-file'),
]