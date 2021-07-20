from django.urls import path

from . import views

urlpatterns = [
    path('cadastro/', views.SignUp.as_view(), name='signup'),
]
