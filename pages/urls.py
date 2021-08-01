from django.urls import path

from . import views

urlpatterns = [
    path('pages/<int:id>/', views.pages, name='pages'),
    path('newPages/<int:id>/', views.newPages, name='new-pages'),

]