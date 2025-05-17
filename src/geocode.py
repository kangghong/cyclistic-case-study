## Functions for reverse geocoding, coordinate-to-station mapping, distance calculations (eg. using geopy)

# utils/geocode.py
import pandas as pd
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import geopandas as gpd
from folium.plugins import HeatMap
import folium


# geolocator = Nominatim(user_agent="cyclistic_project")

'''def reverse_geocode(data, type, pause=1.0):
    """
    Convert latitude and longitude to a station name or location label.
    
    Parameters:
        lat (float): Latitude
        lon (float): Longitude
        pause (float): Delay to avoid rate-limiting
    
    Returns:
        str: Station/location name
    """

    for index, row in data.iterrows():
        
        try:
            location = geolocator.reverse((row[f"{type}_lat"], row[f"{type}_lng"]), exactly_one=True)
            time.sleep(pause)
            data.at[index, f"{type}_station_name"] = location.address.split(",",1)[0]
        
        except Exception as e:
            return f"Error: {e}"
        
    return data
'''
'''def reverse_geocode(data, type_col, pause=1.0):
    """
    Adds a new column to the DataFrame with reverse-geocoded station names using lat/lon.
    Avoids redundant lookups with caching.

    Parameters:
        data (pd.DataFrame): Input DataFrame with lat/lon columns
        type_col (str): Either 'start' or 'end'
        pause (float): Delay between API calls

    Returns:
        pd.DataFrame: With new column: '<type_col>_station_name'
    """
    from collections import defaultdict

    cache = {}
    station_names = []

    for index, row in data.iterrows():
        lat = row[f"{type_col}_lat"]
        lon = row[f"{type_col}_lng"]
        key = (lat, lon)

        if pd.isnull(lat) or pd.isnull(lon):
            station_names.append(None)
            continue

        if key in cache:
            station_names.append(cache[key])
        else:
            try:
                location = geolocator.reverse((lat, lon), exactly_one=True)
                time.sleep(pause)
                if location:
                    station = location.address.split(",", 1)[0]
                    cache[key] = station
                    station_names.append(station)
                else:
                    station_names.append(None)
            except Exception as e:
                print(f"Geocoding failed at index {index}: {e}")
                station_names.append(None)

    data[f"{type_col}_station_name"] = station_names
    return data
'''

def calculate_distance(data):
    """
    Calculate distance between two coordinate points (in km).
    
    Parameters:
        coord1 (tuple): (lat1, lon1)
        coord2 (tuple): (lat2, lon2)
    
    Returns:
        float: Distance in kilometers
    """
    data['ride_distance(km)'] = data.apply(
        lambda row: geodesic((row['start_lat'], row['start_lng']), 
                             (row['end_lat'], row['end_lng'])).kilometers, axis=1).round(3)

    return data

def generate_heatmap(data, membership_status):

    sampled_data = data.sample(frac=0.01)

    gdf = gpd.GeoDataFrame(sampled_data, geometry=gpd.points_from_xy(sampled_data.start_lng, sampled_data.start_lat))

    map_center = [gdf['start_lat'].mean(), 
                  gdf['start_lng'].mean()]
    
    mymap = folium.Map(location=map_center, zoom_start=12)

    # Create a heatmap layer
    heat_data = [[row['start_lat'], row['start_lng']] for _, row in sampled_data.iterrows()]
    
    HeatMap(heat_data).add_to(mymap)

    # Save the map to an HTML file
    mymap.save(f"cyclistic-start-heatmap_{membership_status}.html")

