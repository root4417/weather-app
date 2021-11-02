from django.urls import path
from requests.models import cookiejar_from_dict

from . import views

urlpatterns = [
    path('', views.index),
    path('days/', views.days)
]