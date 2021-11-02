from django.contrib import admin

# Register your models here.
from .models import Weather_csv
from import_export.admin import ImportExportModelAdmin

@admin.register(Weather_csv)
class weatherData(ImportExportModelAdmin):
    pass