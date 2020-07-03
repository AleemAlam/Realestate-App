from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_property, name = 'all_property'),
    path('search/', views.search, name = 'search'),
    path('<int:pk>/', views.single_property, name = 'single_property'),
]
