## Functions for data cleaning
import pandas as pd

def nullProportions (data):

    n_rows = int(data.shape[0])

    null_percents = {}


    for col in data.columns:

        null_percents[col] = { "prop": (int(data[col].isnull().sum())/ n_rows)*100 ,
                              "count": int(data[col].isnull().sum())
                              }

    return null_percents

def verifyConcat (past_year_data, merged_data):
    
    totalRows = 0

    for data in past_year_data:

        totalRows += data.shape[0]

    return totalRows == merged_data.shape[0]

def format_latlon(data):

    latlons = ['start_lat', 'start_lng', 'end_lat', 'end_lng']

    for latlon in latlons:
        data[latlon] = pd.to_numeric(data[latlon], errors = 'coerce').round(6)


    return data

def time_to_minutes(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 60 + m + s / 60

def extract_hour(data):

    start_timestamp = pd.to_datetime(data['started_at'], format='mixed')

    data['start_hour'] = start_timestamp.dt.hour

    return data

def extract_weekday(data):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    start_timestamp = pd.to_datetime(data['started_at'])
    end_timestamp = pd.to_datetime(data['ended_at'])

    data['start_day'] = start_timestamp.dt.dayofweek.map(lambda day:days[day])
    data['end_day'] = end_timestamp.dt.dayofweek.map(lambda day:days[day])

    return data

def extract_month(data):

    data['month'] = pd.to_datetime(
        data['started_at'], 
        format='mixed'
        ).dt.strftime('%B')
    
    return data

def formatTime (timeDelta):
    
    days = timeDelta.components.days
    hrs = days *24 + timeDelta.components.hours
    mins = timeDelta.components.minutes
    secs = timeDelta.components.seconds
  

    return f"{hrs:02}:{mins:02}:{secs:02}"
