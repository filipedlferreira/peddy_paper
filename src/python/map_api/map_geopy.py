from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Peddy_paper")

def parse_geolocator_reverse(location):
    location_dict = {}
    keys_get = ["country","road","city","postcode","county"]

    for i in keys_get:
        location_dict[i] = location.raw["address"][i]
    
    for x in ["lat","lon"]:
        location_dict[x]= location.raw[x]

    return location_dict

def parse_geolocator_geocode(location):
    return

def get_street_name_from_coordinates(location_var):
    full_address = (', ').join([location_var["road"],location_var["city"],location_var["postcode"],location_var["county"],location_var["country"]])
    return full_address

#location = geolocator.geocode("Rua António Feliciano de Castilho, Rio Tinto, 4425-653, Porto, Portugal")
location = geolocator.reverse("41.18506195876603, -8.582049109544942")
location_var = parse_geolocator_reverse(location)
address_1 = get_street_name_from_coordinates(location_var)
print(address_1)
#print(location.latitude, location.longitude)


