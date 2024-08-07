from django.urls import path
from .views import itinerary_api_view , itinerary_view, show_trips

urlpatterns = [
    path('api/', itinerary_api_view, name='itinerary_api'),
    path('trips/', show_trips, name='show_trips'),
    path('itinerary_view/', itinerary_view, name='itinerary_view'),
]