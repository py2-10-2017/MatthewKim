SELECT countries.name, cities.name, district, cities.population FROM countries
JOIN cities ON countries.id=cities.country_id
WHERE district="Buenos Aires" AND cities.population>500000