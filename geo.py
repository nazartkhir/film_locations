from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
from geopy.exc import GeocoderServiceError


def read():
    with open('new_locations.csv', encoding='UTF-8') as file:
        data = file.read().splitlines()
        for i, row in enumerate(data):
            data[i] = row.split('|')
    return data

def get_cords(address):
    geolocator =Nominatim(user_agent="http")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)

def write_cords(a, b):
    with open("new_locations_wcords.csv", 'a', encoding='UTF-8') as file:
        data = read()[a:b]
        for row in data:
            try:
                cords = get_cords(row[2])
                row.append(str(cords[0]))
                row.append(str(cords[1]))
                file.write('|'.join(row))
                file.write('\n')
            except (AttributeError, GeocoderUnavailable, TimeoutError, GeocoderServiceError):
                continue
            

write_cords(14000,15000)