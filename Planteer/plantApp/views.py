from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Plant
# Create your views here.


def all_plants_view(request: HttpRequest):

    plants = Plant.objects.all()
    return render(request, 'all_plants.html', context={'plants':plants})

def plant_details_view(request: HttpRequest, plant_id:int):
    print(plant_id)
    try:
        plant = Plant.objects.get(pk=plant_id)
        print(plant.name)
        request = render(request, 'plant_details.html', context={'plant': plant})
        return request
    except Exception as e:
        return render(request, 'page_not_found.html')
        print(e)

def new_plant_view(request: HttpRequest):

    if request.method == "POST":
        new_plant = Plant(

            name=request.POST['name'],
            about=request.POST['about'],
            used_for=request.POST['used_for'],
            image=request.FILES['image'],
            category=request.POST['category'],
            is_edible=request.POST['is_edible'],
        )

        new_plant.save()
        print(request.POST)
        request = redirect('plantApp:all_plants_view')
        return request

    request = render(request, 'new_plant.html')
    return request


