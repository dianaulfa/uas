
from django.contrib import admin
from django.urls import path
from kedai.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
 
    
]
