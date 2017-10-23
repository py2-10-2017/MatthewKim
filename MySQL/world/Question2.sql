SELECT countries.name, COUNT(cities.id) FROM countries
JOIN cities on countries.id=cities.country_id
GROUP BY countries.id
ORDER BY COUNT(cities.id) DESC