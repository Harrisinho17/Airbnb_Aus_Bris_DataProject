SELECT 
	neighbourhood,
	room_type,
	1 - (AVG(availability_365)/365) AS avg_occupancy_rate
FROM listings
Where availability_365 BETWEEN 10 AND 335
GROUP BY room_type, neighbourhood
ORDER BY neighbourhood, avg_occupancy_rate DESC;

-- This SQL Query goes into the listings table to return a table view of occupancy rates grouped by the types of rooms and the neighbourhood that they are in. I used the aggregate function AVG to get the occupancy rate of different listings in Brisbane. I also wanted to remove listings that could skew the data like listings with partial to no availability or if it was available all year long as this could have been an error or a brand new listing that dosnt have enough data to be calculated yet. 


SELECT 
	room_type,
	1 - (AVG(availability_365)/365) AS avg_occupancy_rate
FROM listings
Where availability_365 BETWEEN 10 AND 335
GROUP BY room_type
ORDER BY avg_occupancy_rate DESC

-- This SQL Query returned a 4 row list with the different room types stored on Airbnb in Brisbane, QLD. This can help breakdown not only how occupancy rates vary across different property types in Brisbane but also you can see what types of properties perform the best 