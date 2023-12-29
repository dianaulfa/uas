from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.kedai, name='kedai.html'),
    path('',views.harga, name='harga.html'),
]