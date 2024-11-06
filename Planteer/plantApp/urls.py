from django.urls import path
from . import views
app_name = 'plantApp'

urlpatterns = [
    path('all/', views.all_plants_view, name='all_plants_view'),
    path('new/', views.new_plant_view, name='new_plant_view'),



]