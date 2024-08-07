import pandas as pd
from api.models import Hotel, Restaurant , Place

def load_hotels():
    hotels = pd.read_csv('hotels.csv')
    for _, row in hotels.iterrows():
        Hotel.objects.create(
            property_name=row['property_name'],
            hotel_star_rating=row['hotel_star_rating'],
            hotel_facilities=row['hotel_facilities'],
            address=row['address'],
            city=row['city'],
            locality=row['locality']
        )

def load_restaurants():
    restaurants = pd.read_csv('restaurant.csv')
    for _, row in restaurants.iterrows():
        Restaurant.objects.create(
            restaurant_name=row['Restaurant Name'],
            cuisine=row['Cuisine'],
            rating=row['Rating'],
            average_price=row['Average Price'],
            area=row['Area'],
            location=row['Location']
        )

def load_places():
    places = pd.read_csv('places.csv')
    for _, row in places.iterrows():
        Place.objects.create(
            zone=row['Zone'],
            state=row['State'],
            city=row['City'],
            name=row['Name'],
            place_type=row['Type'],
            establishment_year=row['Establishment Year'],
            time_needed_to_visit=row['time needed to visit in hrs'],
            google_review_rating=row['Google review rating'],
            entrance_fee=row['Entrance Fee in INR'],
            airport_within_50km=row['Airport with 50km Radius'],
            weekly_off=row['Weekly Off'],
            significance=row['Significance'],
            dslr_allowed=row['DSLR Allowed'],
            number_of_google_reviews=row['Number of google review in lakhs'],
            best_time_to_visit=row['Best Time to visit']
        )

def load_data():
    load_hotels()
    load_restaurants()
    load_places()        