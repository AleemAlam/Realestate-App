from django.shortcuts import render
from .models import HomeProperty
from listings.models import Property
from agents.models import Agent
from .choices import state_choice,bedroom_choices,price_choices,property_type,sqft_choice,bathroom_choices
# Create your views here.

def index(request):
    agents = Agent.objects.all()
    home_property = HomeProperty.objects.all().order_by('-added_date')
    latest_property = Property.objects.all().order_by('-added_date')
    context = {
    'latest_property':latest_property,
    'home_property':home_property,
    'agents':agents,
    'state_choice':state_choice,
    'bedroom_choices':bedroom_choices,
    'bathroom_choices':bathroom_choices,
    'price_choices':price_choices,
    'property_type':property_type,
    'sqft_choice':sqft_choice
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')


def contact(request):
    return render(request,'pages/contact.html')
