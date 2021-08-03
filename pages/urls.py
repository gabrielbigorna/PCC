from django.urls import path

from . import views

urlpatterns = [
    path('pages/<int:id>/', views.pages, name='pages'),
    path('pages/back/', views.backPage, name='back-page'),
    path('pages/url/', views.urlPage, name='url-page'),


]