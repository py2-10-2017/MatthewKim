SELECT cities.name, cities.population FROM countries
JOIN cities ON countries.id=cities.country_id
WHERE countries.name="Mexico"