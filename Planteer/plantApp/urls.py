from django.urls import path
from . import views
app_name = 'plantApp'

urlpatterns = [
    path('all/', views.all_plants_view, name='all_plants_view'),
    path('new/', views.new_plant_view, name='new_plant_view'),
    path('<plant_id>/details/', views.plant_details_view, name="plant_details_view"),
    path('<plant_id>/update/', views.update_plant_view, name="update_plant_view"),
]