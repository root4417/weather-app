from django.db import models

# Create your models here.
class Weather_csv(models.Model):
    number = models.IntegerField()
    description = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)

    class Meta : 
        db_table = 'Weather_csv'