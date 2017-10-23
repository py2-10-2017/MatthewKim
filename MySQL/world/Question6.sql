SELECT countries.name, government_form, capital, life_expectancy FROM countries
WHERE capital>200 AND life_expectancy>75 AND government_form="Constitutional Monarchy"