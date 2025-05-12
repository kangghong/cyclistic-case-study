## Functions for analyzing trip trends
import pandas as pd

def calculateTimeDiff (df) :

    df['started_at'] = pd.to_datetime(df['started_at'], format='mixed', errors='coerce')
    df['ended_at'] = pd.to_datetime(df['ended_at'], format='mixed', errors='coerce')

    time_diff = pd.to_timedelta(df['ended_at'] - df['started_at'])

    df['ride_length'] = time_diff.apply(formatTime)

    return df

def formatTime (timeDelta):
    
    days = timeDelta.components.days
    hrs = days *24 + timeDelta.components.hours
    mins = timeDelta.components.minutes
    secs = timeDelta.components.seconds
  

    return f"{hrs:02}:{mins:02}:{secs:02}"

def extract_weekday(data):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    start_timestamp = pd.to_datetime(data['started_at'])
    end_timestamp = pd.to_datetime(data['ended_at'])

    data['start_day'] = start_timestamp.dt.dayofweek.map(lambda day:days[day])
    data['end_day'] = end_timestamp.dt.dayofweek.map(lambda day:days[day])

    return data

def extract_month(data):

    data['month_idx'] = pd.to_datetime(
        data['started_at'], 
        format='mixed'
        ).dt.month
    
    return data

def season_match (data, season):

    seasons = {'spring': [3,4,5],
               'summer': [6,7,8],
               'autumn': [9,10,11],
               'winter': [12,1,2]}
    
    data = data.loc[data['month_idx'].isin(seasons[season])]

    return data