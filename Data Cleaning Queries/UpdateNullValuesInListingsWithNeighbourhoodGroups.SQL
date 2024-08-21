UPDATE public.listings
SET neighbourhood_group = n.neighbourhood_group
FROM public.neighbourhoods n
WHERE public.listings.neighbourhood = n.neighbourhood
AND public.listings.neighbourhood_group IS NULL;

-- You cannot initialize an abbreviation in the set statement in PostgreSQL