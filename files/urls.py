from django.urls import path

from . import views

urlpatterns = [
    path('', views.files, name='files'),
    path('files/', views.files, name='files'),
    
    path('view/<int:id>/', views.fileView, name='file-view'),
    path('files/view/<int:id>/', views.fileView, name='file-view'),
    
    path('newFile/', views.newFile, name='new-file'),
    path('files/newFile/', views.newFile, name='new-file'),
    
    path('edit/<int:id>', views.editFile, name='edit-file'),
    path('files/edit/<int:id>', views.editFile, name='edit-file'),
    
    path('delete/<int:id>', views.deleteFile, name='delete-file'),
    path('files/delete/<int:id>', views.deleteFile, name='delete-file'),
]
