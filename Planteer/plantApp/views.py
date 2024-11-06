from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def all_plants_view(request: HttpRequest):

    return render(request, 'all_plants.html')


def new_plant_view(request: HttpRequest):
    return render(request, 'new_plant.html')


def contact_messages_view(request: HttpRequest):
    return render(request, 'contact.html')
