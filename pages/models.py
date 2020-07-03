from django.db import models
from agents.models import Agent
from multiselectfield import MultiSelectField

# Create your models here.

PROPERTY_CHOICE = (
    ('House','House'),
    ('Vila','Vila'),
    ('Apartment','Apartment'),
)

CONTRACT_TYPE = (
    ('rent', 'Rent'),
    ('sale', 'Sale'),
)

AMENITIES = (
    ('AC','Air Condition'),
    ('BC','Balcony'),
    ('BK','Built-in-Kitchen'),
    ('D','Dryer'),
    ('FP','Fire Place'),
    ('FF','Fully Furnished'),
    ('G','Gym'),
    ('H','Heating'),
    ('P','Pool'),
    ('S','Storage'),
    ('W','Washer'),
)

class HomeProperty(models.Model):
    agent = models.ForeignKey(Agent , related_name='best_property_agent', on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.IntegerField( blank=True)
    bedroom = models.IntegerField( blank=True)
    bathroom = models.IntegerField( blank=True)
    garage = models.IntegerField( blank=True)
    amenities = MultiSelectField(choices = AMENITIES, max_length = 30 , blank=True)
    mobile_number = models.CharField(max_length = 15, blank=True)
    year_built = models.CharField(max_length = 4, blank=True)
    build_area = models.IntegerField( blank=True)
    sqft = models.IntegerField( blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    desciption = models.TextField(blank = True)
    property_type = models.CharField(choices = PROPERTY_CHOICE, max_length=20, blank=True)
    contract_type = models.CharField(choices = CONTRACT_TYPE, max_length=20, blank=True)
    added_date = models.DateTimeField(blank=True)
    main_image = models.ImageField(upload_to = 'listings/property image')
    image1 = models.ImageField(upload_to = 'listings/property image', blank=True)
    image2 = models.ImageField(upload_to = 'listings/property image', blank=True)
    image3 = models.ImageField(upload_to = 'listings/property image', blank=True)
    image4 = models.ImageField(upload_to = 'listings/property image', blank=True)
    image5 = models.ImageField(upload_to = 'listings/property image', blank=True)
    image6 = models.ImageField(upload_to = 'listings/property image', blank=True)
    def __str__(self):
            return self.title
