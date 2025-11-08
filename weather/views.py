from django.shortcuts import render
import requests

def index(request):
    api_key = "f8fb469678bf1d6bc87f2d9f43340d6b"
    city = "London"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    print(url)

    res = requests.get(url).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }

    context = {
        'info': city_info
    }

    return render(request, 'weather/index.html', context)
