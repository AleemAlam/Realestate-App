from django.contrib import admin
from .models import Property

class PropertyList(admin.ModelAdmin):
    list_display = ('id','title','is_published', 'contract_type' ,'price','added_date','agent')
    list_display_links = ('id','title')
    list_filter = ('agent','is_published')
    search_fields = ('title','desciption', 'address', 'city','state','zipcode')
    list_per_page = 25
    list_editable = ('is_published', 'contract_type' ,'price','added_date','agent')

admin.site.register(Property,PropertyList)
