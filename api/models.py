from django.db import models

# Create your models here.
class Hotel(models.Model):
    property_name = models.CharField(max_length=255)
    hotel_star_rating = models.CharField(max_length=255)
    hotel_facilities = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=255)
    rating = models.CharField(max_length=50)
    average_price = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class Place(models.Model):
    zone = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    place_type = models.CharField(max_length=100)
    establishment_year = models.CharField(max_length=50)
    time_needed_to_visit = models.CharField(max_length=50)
    google_review_rating = models.CharField(max_length=50)
    entrance_fee = models.CharField(max_length=50)
    airport_within_50km = models.CharField(max_length=100)
    weekly_off = models.CharField(max_length=50)
    significance = models.TextField()
    dslr_allowed = models.CharField(max_length=50)
    number_of_google_reviews = models.CharField(max_length=50)
    best_time_to_visit = models.CharField(max_length=100)

# 

class Trip(models.Model):
    city = models.CharField(max_length=100)
    num_days = models.IntegerField()
    itinerary = models.JSONField()

    def __str__(self):
        return f"{self.city} - {self.num_days} days"