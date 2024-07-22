# Airbnb Australia Brisbane Data Project

## Overview

This project is designed for exploring Airbnb listings data in Australia. The queries demonstrate a range of SQL techniques including aggregations, window functions, joins, subqueries, and data type conversions. By using these queries, you can gain insights into various aspects of the Airbnb dataset, such as average prices and number of listings by city, price rankings within cities, and listings with prices above the average in their respective cities. Additional queries cover the integration of listing details with host information, identification of listings with recent reviews, and categorization of listings by price range.

Moreover, the repository includes advanced SQL operations such as searching for listings containing specific keywords in their names, filtering listings based on specific amenities, and calculating monthly availability for listings. A key feature of these queries is the handling of data type conversions to ensure accurate sorting and calculations, exemplified by converting price values from text to numeric formats. This collection is a comprehensive demonstration of SQL capabilities applied to real-world data, providing a robust foundation for anyone looking to enhance their SQL skills using Airbnb data.

## Features

- **SQL Techniques**: Aggregations, window functions, joins, subqueries, and data type conversions.
- **Data Analysis**: Insights into average prices, listings by city, price rankings, and listings above average prices.
- **Advanced SQL Operations**: Keyword search in listings, filtering based on amenities, and calculating monthly availability.

## Project Structure

- **SQL Scripts**: Contains SQL queries for data exploration.
  - `Alter_Table_Price.SQL`
  - `ListingsWith_BedBath_in_90.SQL`
- **Python Script**: Script for data processing.
  - `CsvToTable.py`
- **Data Files**: Includes CSV files with Airbnb listings data.
  - `listings.csv`
  - `neighbourhoods.csv`
  - `neighbourhoods.geojson`
  - `reviews.csv`


## Ackonwledgements 

The data used within this project was sourced from InsideAirbnb.com 