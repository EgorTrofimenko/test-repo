from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def list_of_cars(request):
    return render(request, 'main/list_of_cars.html')


def conditions(request):
    return render(request, 'main/conditions.html')


def service(request):
    return render(request, 'main/service.html')


def contacts(request):
    return render(request, 'main/contacts.html')
