from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

from .config import WEATHER_URL

def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(WEATHER_URL.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)
        

    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)
