# Generated by Django 4.0 on 2021-12-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather_csv',
            name='day',
            field=models.CharField(default='', max_length=100),
        ),
    ]
