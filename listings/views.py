from django.shortcuts import render, get_object_or_404
from .models import Property
from pages.choices import state_choice,bedroom_choices,price_choices,property_type,sqft_choice,bathroom_choices

def all_property(request):
    properties = Property.objects.all().filter(is_published=True)
    context = {
    'properties': properties,
    'state_choice':state_choice,
    'bedroom_choices':bedroom_choices,
    'bathroom_choices':bathroom_choices,
    'price_choices':price_choices,
    'property_type':property_type,
    'sqft_choice':sqft_choice,
    }
    return render(request, 'listings/all_listings.html', context)

def single_property(request, pk):
    property1 = get_object_or_404(Property, pk = pk)
    return render(request, 'listings/single_property.html', {'property1': property1})

def search(request):
    properties = Property.objects.order_by('-added_date').filter(is_published=True)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            properties = properties.filter(city__iexact=city)
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            properties = properties.filter(state__iexact=location)
    if 'property_type' in request.GET:
        property_type = request.GET['property_type']
        if property_type:
            properties = properties.filter(property_type__iexact=location)
    if 'bedroom' in request.GET:
        bedroom = request.GET['bedroom']
        if bedroom:
            properties = properties.filter(bedroom__iexact=location)
    if 'bathroom' in request.GET:
        bathroom = request.GET['bathroom']
        if bathroom:
            properties = properties.filter(bathroom__iexact=location)

    context = {
    'properties': properties,
    'state_choice':state_choice,
    'bedroom_choices':bedroom_choices,
    'bathroom_choices':bathroom_choices,
    'price_choices':price_choices,
    'property_type':property_type,
    'sqft_choice':sqft_choice,
    }
    return render(request, 'listings/search.html',context)
