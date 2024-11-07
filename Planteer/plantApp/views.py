from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Plant
# Create your views here.


def all_plants_view(request: HttpRequest):

    plants = Plant.objects.all()
    return render(request, 'all_plants.html', context={'plants':plants})


def plant_details_view(request: HttpRequest, plant_id:int):

    try:
        plant = Plant.objects.get(pk=plant_id)

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
        
        request = redirect('plantApp:all_plants_view')
        return request

    request = render(request, 'new_plant.html')
    return request

def update_plant_view(request: HttpRequest, plant_id):

    plant = Plant.objects.get(pk=plant_id)

    if request.method == "POST":

        plant.name = request.POST['name']
        plant.about = request.POST['about']
        plant.used_for = request.POST['used_for']
        plant.category = request.POST['category']
        plant.is_edible = request.POST['is_edible']

        if 'image' in request.FILES: plant.image = request.FILES['image']
        plant.save()

        return redirect('plantApp:plant_details_view', plant_id=plant.id)

    return render(request, 'update_plant.html', context={'plant': plant})
