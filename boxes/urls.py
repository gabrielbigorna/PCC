from django.urls import path

from . import views

urlpatterns = [
    path('boxes/', views.boxes, name='boxes'),
    path('boxes/view/<int:id>/', views.boxView, name='box-view'),
    path('boxes/newBox/', views.newBox, name='new-box'),
    path('boxes/edit/<int:id>', views.editBox, name='edit-box'),
    path('boxes/delete/<int:id>', views.deleteBox, name='delete-box'),
    
]
