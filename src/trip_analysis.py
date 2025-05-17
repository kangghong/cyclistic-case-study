## Functions for analyzing trip trends
import pandas as pd
from data_cleaning import formatTime



def calculateTimeDiff (df) :

    df['started_at'] = pd.to_datetime(df['started_at'], format='mixed', errors='coerce')
    df['ended_at'] = pd.to_datetime(df['ended_at'], format='mixed', errors='coerce')

    time_diff = pd.to_timedelta(df['ended_at'] - df['started_at'])

    df['ride_length'] = time_diff.apply(formatTime)

    return df


def season_match (data, season):

    seasons = {'spring': ['March','April','May'],
               'summer': ['June','July','August'],
               'autumn': ['September','October','November'],
               'winter': ['December','January','February']}
    
    data = data.loc[data['month'].isin(seasons[season])]

    return data


def filter_unfeasible_rides(data):
    """
    Filter out rows where the distance covered is not possible based on the ride_length (in minutes).
    
    Parameters:
    - data: DataFrame containing columns 'distance_km', 'ride_length_min', and 'vehicle_type'.
    - max_speeds: Dictionary mapping vehicle types to their maximum feasible speeds in km/h.
    
    Returns:
    - Filtered DataFrame with only feasible rows.
    """
    max_speeds = {
    'electric_bike': 30,  # km/h
    'classic_bike': 20,   # km/h
    'electric_scooter': 25  # km/h
    }

    # Convert ride_length from minutes to hours
    data['ride_length_hours'] = data['ride_length(min)'] / 60
    
    # Calculate the maximum possible distance based on vehicle type
    data['max_possible_distance'] = data.apply(lambda row: row['ride_length_hours'] * max_speeds[row['rideable_type']], axis=1)
    
    # Filter rows where actual distance exceeds the maximum possible distance
    feasible_data = data.loc[data['ride_distance(km)'] <= data['max_possible_distance']]
    
    # Drop the temporary columns
    feasible_data = feasible_data.drop(columns=['ride_length_hours', 'max_possible_distance'])
    
    return feasible_data