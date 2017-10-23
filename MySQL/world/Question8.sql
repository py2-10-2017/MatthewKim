SELECT region, COUNT(countries.id) as Countries FROM countries
GROUP BY region
ORDER BY COUNT(countries.id) DESC