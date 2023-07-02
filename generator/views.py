from django.shortcuts import render
from .models import Photo, GeneratedPhoto


def home(request):
    photos = GeneratedPhoto.objects.all()
    return render(request, 'home.html', {'photos': photos})


def generate(request):
    return render(request, 'generate.html')
