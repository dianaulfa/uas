from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact'),
    
    

]