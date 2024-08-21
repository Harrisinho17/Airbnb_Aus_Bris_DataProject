# Airbnb Market Analysis in Brisbane, QLD

## Overview

This project is a detailed analysis of the Airbnb market in Brisbane, Queensland, aimed at uncovering key insights that can drive decision-making for hosts and stakeholders. The analysis delves into various aspects of the market, including pricing trends, occupancy rates, host performance, and customer satisfaction. By leveraging advanced SQL techniques, Python, and data visualization tools, this project seeks to identify growth opportunities, optimize pricing strategies, and enhance overall market competitiveness.

This project not only serves as a practical application of data analysis skills but also as a demonstration of the power of SQL in handling real-world data. The insights derived will be instrumental in helping Airbnb hosts maximize their revenue and improve guest experiences by making informed, data-driven decisions.


## Key Questions

### Market Trends and Performance
1. **What are the average daily rates (ADR) in different neighborhoods of Brisbane, and how do they compare?**

2. **How do occupancy rates vary across different property types (e.g., entire home, private room) in Brisbane?**

3. **What are the seasonal trends in booking patterns and pricing in Brisbane?**

4. **Which neighborhoods in Brisbane are experiencing the fastest growth in listings and why?**

### Host and Property Insights
5. **What are the most common amenities offered by the top-performing listings in Brisbane?**

6. **How does the number of reviews correlate with the average rating and occupancy rate of listings?**

7. **What factors most significantly impact the pricing of Airbnb listings in Brisbane?**

8. **How do Superhost listings perform compared to non-Superhost listings in terms of occupancy and revenue?**

### Revenue and Pricing Optimization
9. **What pricing strategy can maximize revenue for different types of properties in Brisbane?**

10. **How can dynamic pricing models be implemented to adjust prices based on demand, seasonality, and competitor pricing?**

11. **Which listings are underpriced or overpriced based on similar properties in the same area?**

### Competitive Analysis
12. **How does the performance of Brisbane’s Airbnb market compare to other major Australian cities like Sydney or Melbourne?**

13. **What market share do top Airbnb hosts have in Brisbane, and how does it affect competition?**

14. **What are the top-performing listings in terms of revenue, and what characteristics do they share?**

### Customer Insights
15. **What are the most common reasons for negative reviews, and how can hosts address them?**

16. **Which listings have the highest customer retention rates, and what factors contribute to this?**


## Features

- **SQL Techniques**: Aggregations, window functions, joins, subqueries, and data type conversions.
- **Sentiment Analysis**: Evaluation of customer comments to derive sentiment scores, providing numerical insights into customer satisfaction and feedback trends.
- **Data Analysis**: Insights into average prices, listings by city, price rankings, and listings above average prices.
- **Advanced SQL Operations**: Keyword search in listings, filtering based on amenities, and calculating monthly availability.

## Project Structure

- **Airbnb Data**: Includes CSV files with Airbnb listings data.
  - **Initial Data**
  - `listings.csv`
  - `neighbourhoods.csv`
  - `neighbourhoods.geojson`
  - `reviews.csv`
  
  - **Cleaned Data**
  - `ID_Date.reviews.csv`
  - `comments_with_ratings`
  - `Pre_Cleaning.calendar.csv` 
  - `Pre_Cleaning.ID_Date.Reviews.csv` 
  - `Pre_Cleaning.listings.csv` 
  - `Pre_Cleaning.neighbourhoods.csv` 
  - `Pre_Cleaning.review_sentiment.csv` 
  - `Pre_Cleaning.reviews.csv`
  
- **Data Queries**: SQL Scripts for data analysis & insights.
  - `CsvToTable.py`
  - `ConvertSentiment.py`

- **Python**: Python Scripts for data processing.
  - `CsvToTable.py`
  - `ConvertSentiment.py`

- **Query Results**: Resulting CSV from the Data Queries to be used in Tableau to create a dashboard. 
 - ``
 - ``
 - ``
 - ``


- **Tableau Dashboard**: 
  - ``
  
  


## Conclusion
The insights derived from this analysis will provide valuable information to Airbnb hosts and stakeholders, enabling them to make data-driven decisions to optimize their listings, improve customer satisfaction, and increase profitability.

## Ackonwledgements 

The data used within this project was sourced from InsideAirbnb.com 