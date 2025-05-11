## Functions for analyzing trip trends
import pandas as pd

def calculateTimeDiff (df) :

    df['started_at'] = pd.to_datetime(df['started_at'], format='mixed', errors='coerce')
    df['ended_at'] = pd.to_datetime(df['ended_at'], format='mixed', errors='coerce')

    df['ride_length'] = df['ended_at'] - df['started_at']

    return df
