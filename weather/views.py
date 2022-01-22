import json

import requests
from django.http import HttpResponse
from django.shortcuts import render

from .functions import get_seven_days_prediction


def index(request):
    appid = 'bc914f3e0eee264ed492ef9c71dcaf28'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': 'peshawar', 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    if 'weather' in res and len(res['weather']) > 0:
        res_id = res['weather'][0]['id']
        predictions = get_seven_days_prediction(res_id)
        return render(request, 'index.html', {'data': predictions})
    return render(request, 'index.html', {'data': "FETCHED_CURRENT_STATE_FAILED"})


def get_data(request):
    appid = 'bc914f3e0eee264ed492ef9c71dcaf28'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': 'peshawar', 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    res_id = res['id']
    if 'weather' in res and len(res['weather']) > 0:
        res_id = res['weather'][0]['id']
        predictions = get_seven_days_prediction(res_id)
        return HttpResponse(content=json.dumps({'data': predictions}), content_type='application/json')
    else:
        return HttpResponse(status=404)
