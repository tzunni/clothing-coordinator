from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Weather, Shade, Item
from .forms import ItemForm, RemoveItemForm
import urllib.parse
import random

def generator(request):
    return render(request, 'generator.html')

def get_item(request, weather_name, shade_name, accessory_option):
    try:
        weather_name = urllib.parse.unquote(weather_name)
        shade_name = urllib.parse.unquote(shade_name)
        accessory_option = urllib.parse.unquote(accessory_option)

        if weather_name == 'Any':
            weather = None
        else:
            weather = Weather.objects.get(name=weather_name)

        if shade_name == 'Any':
            shade = None
        else:
            shade = Shade.objects.get(name=shade_name)

        def get_random_item(item_type):
            items = Item.objects.filter(type=item_type)
            if weather:
                items = items.filter(weather=weather)
            if shade:
                items = items.filter(shade=shade)
            return random.choice(items) if items.exists() else None

        top = get_random_item('Top')
        bottom = get_random_item('Bottom')
        accessory = None
        if accessory_option == 'Yes':
            accessory = get_random_item('Accessory')
        elif accessory_option == 'Either':
            accessory = get_random_item('Accessory') if random.choice([True, False]) else None
        if top and bottom and (accessory or accessory_option in ['No', 'Either']):
            generated = f'Top: {top.name}, Bottom: {bottom.name}'
            if accessory:
                generated += f', Accessory: {accessory.name}'
            return JsonResponse({'generated': generated})
        else:
            return JsonResponse({'generated': 'No complete outfit found for the selected criteria.'})
    except (Weather.DoesNotExist, Shade.DoesNotExist):
        return JsonResponse({'generated': 'Please select a valid weather and shade.'})

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
