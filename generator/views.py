from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Weather, Shade, Item
from .forms import ItemForm, RemoveItemForm
import urllib.parse
import random

def generator(request):
    return render(request, 'generator.html')

def get_item(request, weather_name, shade_name):
    try:
        weather_name = urllib.parse.unquote(weather_name)  # Decode the URL-encoded weather value
        shade_name = urllib.parse.unquote(shade_name)  # Decode the URL-encoded shade value
        
        if weather_name == 'Any':
            if shade_name == 'Any':
                items = Item.objects.all()
            else:
                shade = Shade.objects.get(name=shade_name)
                items = Item.objects.filter(shade=shade)
        else:
            weather = Weather.objects.get(name=weather_name)
            if shade_name == 'Any':
                items = Item.objects.filter(weather=weather)
            else:
                shade = Shade.objects.get(name=shade_name)
                items = Item.objects.filter(weather=weather, shade=shade)
        
        if items.exists():
            random_item = random.choice(items)
            return JsonResponse({'generated': random_item.name})
        else:
            return JsonResponse({'generated': 'No item found for the selected criteria.'})
    except Weather.DoesNotExist and Shade.DoesNotExist:
        return JsonResponse({'generated': 'Please select a valid weather and shade.'})
    except Weather.DoesNotExist:
        return JsonResponse({'generated': 'Please select a valid weather.'})
    except Shade.DoesNotExist:
        return JsonResponse({'generated': 'Please select a valid shade.'})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_item')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def remove_item(request):
    if request.method == 'POST':
        form = RemoveItemForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item_id']
            item.delete()
            return redirect('remove_item')
    else:
        form = RemoveItemForm()
    return render(request, 'remove_item.html', {'form': form})