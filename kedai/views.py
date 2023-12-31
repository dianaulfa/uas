from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    return render(request, 'kedai/menu.html')

def login(request):
    return render(request, 'kedai/login.html')

def contact(request):
    return render(request, 'kedai/contact.html')


