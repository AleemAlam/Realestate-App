# Generated by Django 3.0.5 on 2020-04-20 11:44

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zipcode', models.IntegerField(blank=True)),
                ('bedroom', models.IntegerField(blank=True)),
                ('bathroom', models.IntegerField(blank=True)),
                ('garage', models.IntegerField(blank=True)),
                ('amenities', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AC', 'Air Condition'), ('BC', 'Balcony'), ('BK', 'Built-in-Kitchen'), ('D', 'Dryer'), ('FP', 'Fire Place'), ('FF', 'Fully Furnished'), ('G', 'Gym'), ('H', 'Heating'), ('P', 'Pool'), ('S', 'Storage'), ('W', 'Washer')], max_length=30)),
                ('mobile_number', models.CharField(blank=True, max_length=15)),
                ('year_built', models.CharField(blank=True, max_length=4)),
                ('build_area', models.IntegerField(blank=True)),
                ('sqft', models.IntegerField(blank=True)),
                ('is_published', models.BooleanField(blank=True, default=False)),
                ('desciption', models.TextField(blank=True)),
                ('property_type', models.CharField(blank=True, choices=[('House', 'House'), ('Vila', 'Vila'), ('Apartment', 'Apartment')], max_length=20)),
                ('contract_type', models.CharField(blank=True, choices=[('rent', 'Rent'), ('sale', 'Sale')], max_length=20)),
                ('added_date', models.DateTimeField(blank=True)),
                ('main_image', models.ImageField(upload_to='listings/property image')),
                ('image1', models.ImageField(blank=True, upload_to='listings/property image')),
                ('image2', models.ImageField(blank=True, upload_to='listings/property image')),
                ('image3', models.ImageField(blank=True, upload_to='listings/property image')),
                ('image4', models.ImageField(blank=True, upload_to='listings/property image')),
                ('image5', models.ImageField(blank=True, upload_to='listings/property image')),
                ('image6', models.ImageField(blank=True, upload_to='listings/property image')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='best_property_agent', to='agents.Agent')),
            ],
        ),
    ]
