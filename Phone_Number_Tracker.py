import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Get the phone number from the user
number = input("Enter Your Phone Number: ")

# Parse the phone number with the default region
default_region = 'BD'
pepnumber = phonenumbers.parse(number, default_region)

# Get the location of the phone number
location = geocoder.description_for_number(pepnumber, "en")
print(location)

# Get the carrier of the phone number
service_pro = phonenumbers.parse(number, default_region)
carrier_name = carrier.name_for_number(service_pro, "en")
print(carrier_name)

# OpenCage API key
api_key = '47de58ee212d4e8f83147b02c465135e'

# Initialize the OpenCage geocoder
geocoder = OpenCageGeocode(api_key)

# Geocode the location
query = str(location)
results = geocoder.geocode(query)
print(results)

# Extract latitude and longitude
if results and len(results) > 0:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat, lng)

    # Create a map with Folium
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    # Save the map to an HTML file
    myMap.save("mylocation.html")
else:
    print("Geocoding failed, no results found.")
