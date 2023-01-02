import geolocation

def get_coordinates():
    location = geolocation.get_geolocation()

    latitude = location['latitude']
    longitude = location['longitude']

    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

get_coordinates()
