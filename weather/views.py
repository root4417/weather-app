from django.shortcuts import render

import requests
from .models import Weather_csv
# Create your views here.

def index(request):

    appid = 'bc914f3e0eee264ed492ef9c71dcaf28'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':'peshawar', 'appid':appid, 'units':'metric'}

    r = requests.get(url=URL, params=PARAMS)
    res = r.json()

    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    humidity = res['main']['humidity']

    return render(request, 'index.html', {'description' : description,
     'icon' : icon, 'temp' : temp, 'humidity' : humidity})

def days(request):
    datas = Weather_csv.objects.all()

    return render(request, 'days.html', {'datas' : datas})