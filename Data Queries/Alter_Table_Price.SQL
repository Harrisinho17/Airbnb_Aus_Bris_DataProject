-- Function to change the data type of price from text to numeric to make ordering by price easier. 


ALTER TABLE "public"."listings"
ALTER COLUMN price TYPE NUMERIC
USING REGEXP_REPLACE(price, '[^\d.]', '', 'g')::NUMERIC