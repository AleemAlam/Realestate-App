from django.db import models
from multiselectfield import MultiSelectField
from agents.models import Agent

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

class Property(models.Model):
    agent = models.ForeignKey(Agent, related_name = 'agent' , on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    garage = models.IntegerField()
    amenities = MultiSelectField(choices = AMENITIES, max_length = 30 )
    mobile_number = models.CharField(max_length = 15)
    year_built = models.CharField(max_length = 4)
    build_area = models.IntegerField()
    sqft = models.IntegerField()
    is_published = models.BooleanField(default=False)
    desciption = models.TextField(blank = True)
    property_type = models.CharField(choices = PROPERTY_CHOICE, max_length=20)
    contract_type = models.CharField(choices = CONTRACT_TYPE, max_length=20)
    added_date = models.DateField()
    main_image = models.ImageField(upload_to = 'listings/property image')
    image1 = models.ImageField(upload_to = 'listings/property image', blank=True)
    image2 = models.ImageField(upload_to = 'listings/property image', blank=True)
    image3 = models.ImageField(upload_to = 'listings/property image', blank=True)
    image4 = models.ImageField(upload_to = 'listings/property image', blank=True)
    image5 = models.ImageField(upload_to = 'listings/property image', blank=True)
    image6 = models.ImageField(upload_to = 'listings/property image', blank=True)
    floor_image = models.ImageField(upload_to = 'listings/property image', blank=True)






    def __str__(self):
        return self.title
