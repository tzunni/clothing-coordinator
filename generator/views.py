from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def generator(request):
    template = loader.get_template('generator.html')
    return HttpResponse(template.render())