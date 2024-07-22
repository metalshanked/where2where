from geopy.geocoders import Nominatim
import geopy.distance
import random
import string


def generate_random_string(length=12):
    """Generates a random string of specified length.

  Args:
    length: The desired length of the random string. Defaults to 12.

  Returns:
    A string containing random characters (letters and digits) of the
    specified length.
  """

    characters = string.ascii_letters + string.digits  # All letters (uppercase & lowercase) and digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


"""
Under 50 miles no travel fee
50-74 miles 50 $ travel  fee
75-99 75 $ travel feel
100-149 100$  travel fee
150 plus 150$ travel fee

"""


def get_geo_address(dict_location_info: dict):
    if dict_location_info:
        geolocator = Nominatim(user_agent=generate_random_string())
        latitude = dict_location_info.get('coords', {}).get('latitude', 0.0)
        longitude = dict_location_info.get('coords', {}).get('longitude', 0.0)
        location = geolocator.geocode(geolocator.reverse((latitude, longitude)).address)
        return location.address


def get_geo_distance(source_location: str, destination_location: str):
    if source_location and destination_location:
        geolocator = Nominatim(user_agent=generate_random_string())
        location_1 = geolocator.geocode(source_location)
        location_2 = geolocator.geocode(destination_location)

        coords_1 = (location_1.latitude, location_1.longitude)
        coords_2 = (location_2.latitude, location_2.longitude)

        return geopy.distance.geodesic(coords_1, coords_2).miles


def calculate_travel_fee(number_of_miles, data_table):
    """Calculates the travel fee based on the distance.

    Args:
      number_of_miles: The total distance traveled in miles.

    Returns:
      The travel fee in dollars, or 0 if no fee applies.
    """

    li_tup_from_to_cost_mi = list(
        zip(list(data_table.values())[0], list(data_table.values())[1], list(data_table.values())[2]))
    for tup in li_tup_from_to_cost_mi:
        if tup[0] <= number_of_miles <= tup[1]:
            return tup[2]

    #{'From(Mi)': [0, 50, 75, 100, 150], 'To(Mi)': [49, 74, 99, 150, 99999], 'Cost(USD)': [0, 50, 75, 100, 150]}
