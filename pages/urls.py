from django.urls import path

from . import views

urlpatterns = [
    path('pages/<int:id>/', views.pages, name='pages'),

]