# Changelog

# Data Cleaning Changelog - Cyclistic Data for the past year

**Date:** 2025-05-11  
**Author:** Cyclistic Marketing Analytics Team

## Summary

Tracks data cleaning steps for 'customer_orders.csv'.

## Version [1.2.0]-(05-13-2025)

### New

### Changes

### Fixes

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
