# Changelog

# Data Cleaning Changelog - Cyclistic Data for the past year

**Date:** 2025-05-11  
**Author:** Cyclistic Marketing Analytics Team

## Summary

Tracks data cleaning steps for 'customer_orders.csv'.

## Version [1.2.0]-(05-14-2025)

### New

    - Added extract_hour function to trip_analysis.py, for analysis of peak hour behaviours
    - Added generate_hist_plot function to user_segmentation.py, as reusable code for generating histogram
    - Added filter_unfeasible_rides function in trip_analysis.py, to single out rides that aren't possible
    - Added .gitattributes file to control Git file handling, included relevant lines
    - Added generate_pie, generate_hist_plot and plot_pivot_table visualization functions
    - Filled in final.ipynb with concised code, and relevant visualizations
    - Filled in requirements.txt with relevant dependencies
    - Added assets folder

### Changes

    - Changed parameter of generate_prop_plot function to an intuitive name
    - Moved time_to_minutes function to data_cleaning.py
    - Changed metrics of data analysis to median, for ride distances and ride times
    - Changed output of extract_month function, to output the month instead of its index
    - Moved extract_month, extract_weekday, extract_hour and formatTime functions to data_cleaning.py
    - Modified barplot of generate_prop_plot function, to not generate stacked bar charts
    - Renamed src file to data_viz.py
    - Improved generalizability of generate_prop_plot function
    - Utilized reusable code for code repeats

### Fixes

    - Fixed generate_prop_plot function to take in the season, as a argument
    - Fixed cell outputs of all notebooks

## Version [1.1.0]-(05-12-2025)

### New

    - Added new columns, (ride_length, ride_distance and start_day)
    - Dropped start_station_name, start_station_id, end_station_name and end_station_id
    - Dropped rows with NULL longitudes and latitudes
    - Complete export of processed dataset
    - Added function to extract weekday from datetime string
    - Introduced user_segmentation.py for behavioural comparisons

### Changes

    - Changed time format of time differences to HH:MM:SS
    - Refactored timedelta parsing to handle inconsistent formats
    - Updated column name of membership_status, for intuitivity

### Fixes

    - Fixed format_latlon output to generate coordinates of 6 decimals
    - Resolved issue with negative trip durations

## Version [1.0.0]-(05-11-2025)

### Initial Release

    - Added /data folder : Raw and processed datasets
    - Added /src folder: Scripts for cleaning, geocoding and analysis
    - Added /utils folder: Scripts for file I/O
    - Added /logs folder: Scripts for changelog
    - Added /notebooks folder: Notebooks for exploration and final analysis
    - Added .gitignore, and venv setup
