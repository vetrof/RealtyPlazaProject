# Import the required library
from geopy.geocoders import Nominatim


def address_to_coordinates(city, street, building):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(f"{city}, {street}, {building}")

    print(f"{city}, {street}, {building}")
    return location.latitude, location.longitude
