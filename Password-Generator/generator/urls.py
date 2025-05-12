from django.urls import path
from . import views

urlpatterns = [
    path('', views.password_requirements, name='password_requirements'),
    path('result/', views.password_result, name='password_result'),
]