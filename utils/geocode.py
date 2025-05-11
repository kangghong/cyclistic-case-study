## Functions for reverse geocoding, coordinate-to-station mapping, distance calculations (eg. using geopy)

# utils/geocode.py

from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="cyclistic_project")

def reverse_geocode(lat, lon, pause=1.0):
    """
    Convert latitude and longitude to a station name or location label.
    
    Parameters:
        lat (float): Latitude
        lon (float): Longitude
        pause (float): Delay to avoid rate-limiting
    
    Returns:
        str: Station/location name
    """
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True)
        time.sleep(pause)
        return location.address if location else "Unknown"
    except Exception as e:
        return f"Error: {e}"

def calculate_distance(coord1, coord2):
    """
    Calculate distance between two coordinate points (in km).
    
    Parameters:
        coord1 (tuple): (lat1, lon1)
        coord2 (tuple): (lat2, lon2)
    
    Returns:
        float: Distance in kilometers
    """
    return geodesic(coord1, coord2).kilometers

def format_latlon(lat, lon):
    """
    Format latitude and longitude to a clean string.
    
    Returns:
        str: Formatted lat/lon
    """
    return f"{lat:.5f}, {lon:.5f}"
