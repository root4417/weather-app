import datetime
import json

import requests
from django.http import HttpResponse
from django.shortcuts import render

from .models import Weather_csv


def index(request):
    data = Weather_csv.objects.all()[:7]

    appid = 'bc914f3e0eee264ed492ef9c71dcaf28'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': 'peshawar', 'appid': appid, 'units': 'metric'}

    r = requests.get(url=URL, params=PARAMS)
    res = r.json()

    description = res['weather'][0]['description']
    res_icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    humidity = res['main']['humidity']
    res_id = res['id']
    cloud = res['clouds']['all']

    day = datetime.date.today()
    data_next_7_days = []
    today_date_day_name = day.strftime("%A").upper()
    today_day_short_name = today_date_day_name[:3]
    print(today_date_day_name)
    for d in data:
        # if d.day.upper() != today_date_day_name:
        if d.description == 'rainy':
            icon = '<i class="wi wi-rain"></i>'
        elif d.description == 'drizzle':
            icon = '<i class="wi wi-raindrops"></i>'
        elif d.description == 'haze':
            icon = '<i class="wi wi-day-haze"></i>'
        elif d.description == 'hot':
            icon = '<i class="wi wi-hot"></i>'
        elif d.description == 'sunny':
            icon = '<i class="wi wi-day-sunny"></i>'
        elif d.description == 'partially-cloud':
            icon = '<i class="wi wi-day-cloudy"></i>'
        elif d.description == 'cloud':
            icon = '<i class="wi wi-cloudy"></i>'
        elif d.description == 'storm' or d.description == 'thunderstorm':
            icon = '<i class="wi wi-storm-showers"></i>'
        elif d.description == 'smog':
            icon = '<i class="wi wi-smog"></i>'
        elif d.description == 'smoke':
            icon = '<i class="wi wi-smoke"></i>'
        elif d.description == 'windy' or d.description == 'winds' or d.description == 'wind':
            icon = '<i class="wi wi-windy"></i>'
        elif d.description == 'hurricane':
            icon = '<i class="wi wi-hurricane"></i>'
        elif d.description == 'snow' or d.description == 'snowing' or d.description == 'snowy':
            icon = '<i class="wi wi-snow"></i>'
        elif d.description == 'dust' or d.description == 'dusty':
            icon = '<i class="wi wi-dust"></i>'
        elif d.description == 'lightning':
            icon = '<i class="wi wi-lightning"></i>'
        elif d.description == 'partly-cloudy':
            icon = '<i class="wi wi-night-partly-cloudy"></i>'
        else:
            icon = '<i class="wi wi-na"></i>'
        data_next_7_days.append({
            'number': d.number,
            'day': d.day.upper()[:3],
            'description': d.description,
            'icon': icon,
            'temperature': d.temperature,
            'humidity': d.humidity,
        })
    found_at_index = 0
    for i, item in enumerate(data_next_7_days):
        if item['day'] == today_day_short_name:
            found_at_index = i
    data_next_7_days[found_at_index] = {
        'number': res_id,
        'day': today_day_short_name,
        'description': description,
        'icon': res_icon,
        'temperature': temp,
        'humidity': humidity,
    }
    print(f'today_day_short_name: {today_day_short_name}')
    day_order = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    i = 0
    while day_order[i] != today_day_short_name:
        day_order.append(day_order.pop(day_order.index(day_order[i])))

    sorted_data = sorted(data_next_7_days, key=lambda d: day_order.index(d["day"][:3]))

    return render(request, 'index.html', {'data': sorted_data})


def get_data(request):
    data = Weather_csv.objects.all()[:7]
    data_objects = []
    for d in data:
        data_objects.append({
            'id': d.id,
            'number': d.number,
            'day': d.day,
            'description': d.description,
            'icon': d.icon,
            'temperature': d.temperature,
            'humidity': d.humidity
        })
    return HttpResponse(content=json.dumps({'data': data_objects}), content_type='application/json')
