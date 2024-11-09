from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Plant
from .forms import PlantForm
# Create your views here.


def all_plants_view(request: HttpRequest):

    plants = Plant.objects.all()

    if 'order_by' in request.GET:
        if request.GET['order_by'] == 'oldest':
            plants = plants.order_by("-created_at")

        elif request.GET['order_by'] == 'newest':
            plants = plants.order_by("created_at")

    if 'category' in request.GET:

        if request.GET['category'] == 'tree':
            plants = Plant.objects.filter(category="tree")

        elif request.GET['category'] == 'fruit':
            plants = Plant.objects.filter(category="fruit")

        elif request.GET['category'] == 'vegetable':
            plants = Plant.objects.filter(category="vegetables")

        elif request.GET['category'] == 'other':
            plants = Plant.objects.filter(category="other")

    if 'is_edible' in request.GET:
        if request.GET['is_edible'] == 'edible':
            plants = Plant.objects.filter(is_edible=True)

        elif request.GET['is_edible'] == 'non-edible':
            plants = Plant.objects.filter(is_edible=False)

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

    plant_form = PlantForm()
    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()

            return redirect('plantApp:all_plants_view')
        else:
            print("Form is Not Valid")

    request = render(request, 'new_plant.html', context={'categories':Plant.PlantsCategories.choices})
    return request


def update_plant_view(request: HttpRequest, plant_id):

    try:
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
    except Exception as e:
        return render(request, 'page_not_found.html')

    return render(request, 'update_plant.html', context={'plant': plant})


def delete_plant_view(request: HttpRequest, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
        plant.delete()
        return redirect('plantApp:all_plants_view')
    except Exception as e:
        return render(request, 'page_not_found.html')


def search_view(request: HttpRequest):

    if 'keyword' in request.GET and len(request.GET['keyword']) >= 3:
        keyword = request.GET['keyword']

        results = Plant.objects.filter(
            Q(name__contains=keyword) |
            Q(about__contains=keyword) |
            Q(category__contains=keyword) |
            Q(used_for__contains=keyword)
        )

    else:
        results = []

    return render(request, 'search_results.html', context={'results': results})


def filter_view(request: HttpRequest):
    pass
    # filter = request.GET['filter']
    #
    # results = Plant.objects.all()

    # return render(request, 'plantApp:all_plants_view', context={'plants': plants})