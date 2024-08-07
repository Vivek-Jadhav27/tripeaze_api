# itinerary/serializers.py

from rest_framework import serializers
from .models import Hotel, Restaurant, Place , Trip

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['property_name', 'address', 'hotel_star_rating', 'hotel_facilities']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'cuisine', 'rating', 'average_price', 'location']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['name', 'place_type', 'google_review_rating', 'entrance_fee', 'significance', 'dslr_allowed']

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'