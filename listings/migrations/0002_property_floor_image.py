# Generated by Django 3.0.5 on 2020-05-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='floor_image',
            field=models.ImageField(blank=True, upload_to='listings/property image'),
        ),
    ]
