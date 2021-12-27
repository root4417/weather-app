from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Weather_csv


@admin.register(Weather_csv)
class weatherData(ImportExportModelAdmin):
    list_display = [
        'id',
        'number',
        'day',
        'description',
        'temperature',
        'humidity',
        'icon'
    ]
