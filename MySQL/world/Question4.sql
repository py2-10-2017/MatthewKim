SELECT name, language, percentage FROM countries
JOIN languages ON countries.id=languages.country_id
WHERE percentage>89
ORDER BY percentage DESC