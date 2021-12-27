from django.urls import path
from requests.models import cookiejar_from_dict

from . import views

urlpatterns = [
    path('', views.index),
    path('get-data/', views.get_data, name='get-data')
]