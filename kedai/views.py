from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'kedai/index.html')

def menu(request):
    return render(request, 'kedai/menu.html')

def harga(request):
    return render(request, 'kedai/harga.html')
