from django.shortcuts import get_object_or_404, redirect, render
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
        res = requests.get(WEATHER_URL.format(city.name))
        res_status_code = res.status_code
        res_json = res.json()

        if res_status_code == 200:
            city_info = {
                'id': city.pk,
                'city': city.name,
                'temp': res_json['main']['temp'],
                'icon': res_json['weather'][0]['icon']
            }

            all_cities.append(city_info)
        

    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)

def delete_city(request, pk):
    item = get_object_or_404(City, pk=pk)
    if request.method == "POST" and request.POST.get("_method") == "delete":
        item.delete()
        return redirect('home')
