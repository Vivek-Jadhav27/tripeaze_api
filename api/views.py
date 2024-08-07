# itinerary/views.py
from django.shortcuts import render
import pandas as pd
import random
from .models import Hotel, Restaurant ,Place, Trip
from .serializers import HotelSerializer, RestaurantSerializer, PlaceSerializer, TripSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Function to generate a Google search URL
def generate_google_search_url(name, city):
    query = f"{name} {city}"
    return f"https://www.google.com/search?q={query.replace(' ', '+')}"

# Function to recommend hotels
def recommend_hotels(city,num_day ,num_recommendations=5):
    city_hotels = Hotel.objects.filter(city__icontains=city)
    if not city_hotels.exists():
        return pd.DataFrame()

    hotel_df = pd.DataFrame(list(city_hotels.values()))
    hotel_df['combined_features'] = hotel_df['hotel_star_rating'].astype(str) + " " + hotel_df['hotel_facilities'].astype(str)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(hotel_df['combined_features'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(hotel_df.index, index=hotel_df['property_name']).drop_duplicates()
    idx = random.choice(hotel_df.index)
    sim_scores = list(enumerate(cosine_sim[hotel_df.index.get_loc(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]
    hotel_indices = [i[0] for i in sim_scores]
    recommended_hotels = hotel_df.iloc[hotel_indices][['property_name', 'address', 'hotel_star_rating', 'hotel_facilities']]
    return recommended_hotels

# Function to recommend restaurants
def recommend_restaurants(city, num_day,num_recommendations=5):
    city_restaurants = Restaurant.objects.filter(location__icontains=city)
    if not city_restaurants.exists():
        return pd.DataFrame()

    restaurant_df = pd.DataFrame(list(city_restaurants.values()))
    restaurant_df['combined_features'] = restaurant_df['cuisine'].astype(str) + " " + restaurant_df['rating'].astype(str)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(restaurant_df['combined_features'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(restaurant_df.index, index=restaurant_df['restaurant_name']).drop_duplicates()
    idx = random.choice(restaurant_df.index)
    sim_scores = list(enumerate(cosine_sim[restaurant_df.index.get_loc(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]
    restaurant_indices = [i[0] for i in sim_scores]
    recommended_restaurants = restaurant_df.iloc[restaurant_indices][['restaurant_name', 'cuisine', 'rating', 'average_price', 'location']]
    return recommended_restaurants

# Function to recommand places
def recommend_places(city,num_day, num_recommendations=5):
    city_places = Place.objects.filter(city__icontains=city)
    if not city_places.exists():
        return pd.DataFrame()
    
    place_df = pd.DataFrame(list(city_places.values()))
    place_df['combined_features'] = place_df['zone'].astype(str) + " " + place_df['state'].astype(str) + " " + place_df['city'].astype(str)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(place_df['combined_features'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(place_df.index, index=place_df['name']).drop_duplicates()
    idx = random.choice(place_df.index)
    sim_scores = list(enumerate(cosine_sim[place_df.index.get_loc(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]
    place_indices = [i[0] for i in sim_scores]
    recommended_places = place_df.iloc[place_indices][['name', 'place_type', 'google_review_rating', 'entrance_fee', 'significance', 'dslr_allowed']]
    return recommended_places
    

# Function to generate an itinerary
def generate_itinerary(city, num_days):
    itinerary = []
    hotels = recommend_hotels(city, num_days, num_recommendations=num_days)
    restaurants = recommend_restaurants(city, num_days, num_recommendations=num_days * 3)
    places = recommend_places(city, num_days, num_recommendations=num_days * 3)
    
    if hotels.empty or restaurants.empty or places.empty:
        return None

    for day in range(1, num_days + 1):
        hotel = hotels.iloc[day - 1] if day - 1 < len(hotels) else hotels.iloc[random.randint(0, len(hotels) - 1)]
        breakfast = restaurants.iloc[day * 3 - 3] if day * 3 - 3 < len(restaurants) else restaurants.iloc[random.randint(0, len(restaurants) - 1)]
        lunch = restaurants.iloc[day * 3 - 2] if day * 3 - 2 < len(restaurants) else restaurants.iloc[random.randint(0, len(restaurants) - 1)]
        dinner = restaurants.iloc[day * 3 - 1] if day * 3 - 1 < len(restaurants) else restaurants.iloc[random.randint(0, len(restaurants) - 1)]
        morning_activity = places.iloc[day * 3 - 3] if day * 3 - 3 < len(places) else places.iloc[random.randint(0, len(places) - 1)]
        afternoon_activity = places.iloc[day * 3 - 2] if day * 3 - 2 < len(places) else places.iloc[random.randint(0, len(places) - 1)]
        itinerary.append({
            'day': day,
            'hotel': {
                'name': hotel['property_name'],
                'rating': hotel['hotel_star_rating'],
                'address': hotel['address'],
                'url': generate_google_search_url(hotel['property_name'], city)
            },
            'breakfast': {
                'name': breakfast['restaurant_name'],
                'rating': breakfast['rating'],
                'location': breakfast['location'],
                'url': generate_google_search_url(breakfast['restaurant_name'], city)
            },
            'morning_activity': {
                'name': morning_activity['name'],
                'type': morning_activity['place_type'],
                'rating': morning_activity['google_review_rating'],
                'entrance_fee': morning_activity['entrance_fee'],
                'significance': morning_activity['significance'],
                'dslr_allowed': morning_activity['dslr_allowed'],
                'url': generate_google_search_url(morning_activity['name'], city)
            },
            'lunch': {
                'name': lunch['restaurant_name'],
                'rating': lunch['rating'],
                'location': lunch['location'],
                'url': generate_google_search_url(lunch['restaurant_name'], city)
            },
             'afternoon_activity': {
                'name': afternoon_activity['name'],
                'type': afternoon_activity['place_type'],
                'rating': afternoon_activity['google_review_rating'],
                'entrance_fee': afternoon_activity['entrance_fee'],
                'significance': afternoon_activity['significance'],
                'dslr_allowed': afternoon_activity['dslr_allowed'],
                'url': generate_google_search_url(afternoon_activity['name'], city)
            },
            'dinner': {
                'name': dinner['restaurant_name'],
                'rating': dinner['rating'],
                'location': dinner['location'],
                'url': generate_google_search_url(dinner['restaurant_name'], city)
            }
        })
    return itinerary

# def itinerary_view(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         num_days = int(request.POST.get('num_days'))
#         itinerary = generate_itinerary(city, num_days)
#         if itinerary is None:
#             return render(request, 'itinerary_error.html')
#         return render(request, 'itinerary_result.html', {'itinerary': itinerary, 'city': city, 'num_days': num_days})
#     return render(request, 'itinerary_form.html')

# @api_view(['GET', 'POST'])
# def itinerary_api_view(request):
#     if request.method == 'POST':
#         city = request.data.get('city')
#         num_days = int(request.data.get('num_days'))
#         itinerary = generate_itinerary(city, num_days)
#         if itinerary is None:
#             return Response({"error": "Unable to generate itinerary."}, status=400)
#         return Response({'itinerary': itinerary, 'city': city, 'num_days': num_days})
#     return Response({"message": "Send a POST request with city and num_days to generate an itinerary."})

def itinerary_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        num_days = int(request.POST.get('num_days'))
        itinerary = generate_itinerary(city, num_days)
        if itinerary is None:
            return render(request, 'itinerary_error.html')
        
        # Save the itinerary as a Trip in the database
        trip = Trip(city=city, num_days=num_days, itinerary=itinerary)
        trip.save()
        
        return render(request, 'itinerary_result.html', {'itinerary': itinerary, 'city': city, 'num_days': num_days})
    return render(request, 'itinerary_form.html')

@api_view(['GET', 'POST'])
def itinerary_api_view(request):
    if request.method == 'POST':
        city = request.data.get('city')
        num_days = int(request.data.get('num_days'))
        itinerary = generate_itinerary(city, num_days)
        if itinerary is None:
            return Response({"error": "Unable to generate itinerary."}, status=400)
        
        # Save the itinerary as a Trip in the database
        trip = Trip(city=city, num_days=num_days, itinerary=itinerary)
        trip.save()
        
        return Response({'itinerary': itinerary, 'city': city, 'num_days': num_days})
    
    return Response({"message": "Send a POST request with city and num_days to generate an itinerary."})

@api_view(['GET'])
def show_trips(request):
    if request.method == 'GET':
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data, status=200)