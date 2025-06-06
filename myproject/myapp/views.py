from django.shortcuts import render, redirect
from .models import Products, Hhoodie, Working


def home(request):
    context = {
        'products': Products.objects.all(),
        'working': Working.objects.all(),
    }
    return render(request, 'second.html', context)


def products(request):
    return redirect('home')  

def working(request):
    return redirect('home')  

def polos(request):
    return render(request, 'polos.html')

def tshirts(request):
    return render(request, 'tshirts.html')

def jackets(request):
    return render(request, 'jackets.html')

def sweatshirts(request):
    return render(request, 'sweatshirts.html')

def hoodie(request):
    hoodies = Hhoodie.objects.all()
    context = {'hoodies': hoodies}
    return render(request, 'hoodies.html', context)


def about(request):
    return render(request, 'aboutus.html')