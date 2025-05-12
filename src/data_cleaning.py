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


