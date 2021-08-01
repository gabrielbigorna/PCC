from django.urls import path

from . import views

urlpatterns = [
    path('', views.boxes, name='boxes'),
    path('boxes/', views.boxes, name='boxes'),
    
    path('view/<int:id>/', views.boxView, name='box-view'),
    path('boxes/view/<int:id>/', views.boxView, name='box-view'),
    
    path('newBox/', views.newBox, name='new-box'),
    path('boxes/newBox/', views.newBox, name='new-box'),
    
    path('edit/<int:id>', views.editBox, name='edit-box'),
    path('boxes/edit/<int:id>', views.editBox, name='edit-box'),
    
    path('delete/<int:id>', views.deleteBox, name='delete-box'),
    path('boxes/delete/<int:id>', views.deleteBox, name='delete-box'),
]
