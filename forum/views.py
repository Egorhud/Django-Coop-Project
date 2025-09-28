from django.shortcuts import render

def home(request):
    """Главная страница сайта"""
    return render(request, 'home.html')