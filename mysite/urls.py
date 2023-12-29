
from django.contrib import admin
from django.urls import path
from kedai.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
    path('harga/', harga, name='harga'),
]
