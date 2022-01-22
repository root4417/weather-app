# -*- coding: UTF-8 -*-
# '''=================================================
# @Project: the_weather
# @File   : functions
# @IDE    : PyCharm
# @Author : Muhammad Arshad
# @Email  : arshad@hexasoft.io
# @Time   : 22/01/2022 4:48 PM
# @Desc   :
# '''=================================================
import datetime
import random


def get_current_weather_state(weather_code):
    if weather_code in [200, 201, 202, 210, 211, 212, 221, 230, 231, 232]:
        # actual Thunderstorm
        return 'R'
    elif weather_code in [300, 301, 302, 310, 311, 312, 313, 314, 321]:
        # actual Drizzle
        return 'D'
    elif weather_code in [500, 501, 502, 503, 504, 511, 520, 521, 522, 531]:
        # actual rain
        return 'R'
    elif weather_code in [600, 601, 602, 611, 612, 613, 615, 616, 620, 621, 622]:
        # actual snow
        return 'R'
    elif weather_code == 800:
        # actual Clear
        return 'S'
    elif weather_code in [801, 802, 803, 804]:
        # actually Cloudy
        return 'PC'
    elif weather_code in [701, 711, 721, 731, 741, 751, 761, 762, 771, 781]:
        # actually Atmosphere different.
        return 'C'


def get_weather_icon(prediction):
    if prediction == "R":
        return 'https://openweathermap.org/img/wn/11d@4x.png'
    elif prediction == "D":
        return 'https://openweathermap.org/img/wn/09d@4x.png'
    elif prediction == "C":
        return 'https://openweathermap.org/img/wn/02d@4x.png'
    elif prediction == "PC":
        return 'https://openweathermap.org/img/wn/04d@4x.png'
    else:
        return 'https://openweathermap.org/img/wn/01d@4x.png'


def get_next_prediction(current_state):
    x = random.random()
    if current_state == "R":
        if 0 < x < 0.2:
            return "D"
        elif 0 < x < 0.3:
            return "R"
        elif 0 < x < 0.55:
            return "C"
        elif 0 < x < 0.85:
            return "PC"
        else:
            return "S"
    elif current_state == "C":
        if 0 < x < 0.15:
            return "D"
        elif 0 < x < 0.3:
            return "R"
        elif 0 < x < 0.45:
            return "C"
        elif 0 < x < 0.75:
            return "PC"
        else:
            return "S"
    elif current_state == "S":
        if 0 < x < 0.05:
            return "D"
        elif 0 < x < 0.1:
            return "R"
        elif 0 < x < 0.2:
            return "C"
        elif 0 < x < 0.4:
            return "PC"
        else:
            return "S"
    elif current_state == "D":
        if 0 < x < 0.15:
            return "D"
        elif 0 < x < 0.45:
            return "R"
        elif 0 < x < 0.7:
            return "C"
        elif 0 < x < 0.95:
            return "PC"
        else:
            return "S"
    elif current_state == "PC":
        if 0 < x < 0.1:
            return "D"
        elif 0 < x < 0.2:
            return "R"
        elif 0 < x < 0.4:
            return "C"
        elif 0 < x < 0.5:
            return "PC"
        else:
            return "S"
    else:
        return "Invalid"


def get_weather_full_name(state):
    if state == "R":
        return "Rainy"
    elif state == "S":
        return "Sunny"
    elif state == "C":
        return "Cloudy"
    elif state == "PC":
        return "Partly Cloudy"
    elif state == "D":
        return "Drizzle"
    else:
        return "Invalid"


def get_next_day_date(current_date):
    return current_date + datetime.timedelta(days=1)


def get_day_name(current_date):
    return current_date.strftime("%A").upper()


def get_seven_days_prediction(current_weather_id):
    seven_days_predictions = []
    date_time_now = datetime.datetime.now()

    current_weather_state = get_current_weather_state(current_weather_id)
    seven_days_predictions.append({
        'date': date_time_now.strftime('%d/%m/%Y'),
        'day': get_day_name(date_time_now),
        'weather_condition': get_weather_full_name(current_weather_state),
        'weather_condition_short_name': current_weather_state,
        'icon': get_weather_icon(current_weather_state)
    })

    for i in range(1, 7):
        date_time_now += datetime.timedelta(days=1)
        previous_weather_state = seven_days_predictions[i-1]['weather_condition_short_name']
        current_weather_state = get_next_prediction(previous_weather_state)
        seven_days_predictions.append({
            'date': date_time_now.strftime('%d/%m/%Y'),
            'day': get_day_name(date_time_now),
            'weather_condition': get_weather_full_name(current_weather_state),
            'weather_condition_short_name': current_weather_state,
            'icon': get_weather_icon(current_weather_state)
        })

    return seven_days_predictions
