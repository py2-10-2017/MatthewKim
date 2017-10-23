SELECT film.film_id, title, description, release_year, rating, special_features, name, rental_rate FROM film
JOIN film_category ON film.film_id=film_category.film_id
JOIN category ON film_category.category_id=category.category_id
WHERE name="Drama" and rental_rate=2.99