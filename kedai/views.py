from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    return render(request, 'kedai/menu.html')

def logo(request):
    return render(request, 'kedai/logo.html')
