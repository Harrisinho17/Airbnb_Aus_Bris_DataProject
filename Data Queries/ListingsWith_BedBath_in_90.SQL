-- Displays a table of all active Airbnb listings in Brisbane, Australia that have availibilty within the next 90 days. 
-- As well as at least 2 bedrooms and ordered by hosy_id and price to group lsitings by the same Host.  

SELECT id, host_id, host_name, bedrooms, bathrooms, price, availability_90, reviews_per_month
FROM "public"."listings"
WHERE bedrooms >= 2
  AND availability_90 >= 1
  AND bathrooms IS NOT NULL
ORDER BY host_id, price DESC