import pandas as pd

def load_csvs(past_year_data):

    may_2024 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202405-divvy-tripdata.csv')
    jun_2024 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202406-divvy-tripdata.csv')
    jul_2024 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202407-divvy-tripdata.csv')
    aug_2024 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202408-divvy-tripdata.csv')
    sep_2024 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202409-divvy-tripdata.csv')
    oct_2024 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202410-divvy-tripdata.csv')
    nov_2024 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202411-divvy-tripdata.csv')
    dec_2024 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202412-divvy-tripdata.csv')
    jan_2025 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202501-divvy-tripdata.csv')
    feb_2025 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202502-divvy-tripdata.csv')
    mar_2025 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202503-divvy-tripdata.csv')
    apr_2025 = pd.read_csv('/Users/kanghong/Documents/Developer/Google-Capstone/cyclist-case-study/data/202504-divvy-tripdata.csv')

    return pd.concat(list(past_year_data), ignore_index=True)