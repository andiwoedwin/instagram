from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='instagram-home'),
    path('about/', views.about, name='instagram-about'),
]