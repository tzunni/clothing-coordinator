# clothing-coordinator
## Students:
- Keith Bui
- Matthew Dzoan
- Jeffrey Wong
- Jacob Sean Evasco
- Wonjun Kim

## Language:
We are using Django as our framework, and also using HTML, CSS, JS, and Python in our project.

## Description:
We want to create a website that will scan in clothing items and generate outfits based off of factors such as weather, season, and other clothing attributes to help people pick their outfits for the day.

## Usage:
run
```bash
py manage.py runserver
```

## Setup:
1. **Open the Django Shell and Import Models:**
   ```sh
   py manage.py migrate generator 0001
   py manage.py shell
   ```

2. **Import our shade and weather states into the database:**
   ```py
   from generator.models import Shade, Weather

   weather_data = ['Cold', 'Temperate', 'Warm', 'Hot']
   shade_data = ['Light', 'Dark']

   for weather in weather_data:
       Weather.objects.create(name=weather)

   for shade in shade_data:
       Shade.objects.create(name=shade)
   ```
