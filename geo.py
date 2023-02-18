from geopy.geocoders import Nominatim

def get_cords(address):
    geolocator =Nominatim(user_agent="http")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)

