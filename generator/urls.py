from django.urls import path
from . import views

urlpatterns = [
    path('', views.generator, name='home'),
]
