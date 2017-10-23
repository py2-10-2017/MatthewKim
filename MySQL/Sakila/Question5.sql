SELECT title, description, release_year, rating, special_features FROM film
JOIN film_actor ON film.film_id=film_actor.film_id
WHERE rating="G" AND special_features LIKE "%Behind the Scenes%" AND actor_id=15