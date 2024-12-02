# generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.generator, name='home'),
    path('generator/<str:weather_name>/<str:shade_name>/<str:accessory_option>/', views.get_item, name='get_item'),
    path('add-item/', views.add_item, name='add_item'),
    path('remove-item/', views.remove_item, name='remove_item'),
]
