SELECT actor.actor_id, CONCAT(first_name,' ',last_name), film.film_id, title, description, release_year FROM film
JOIN film_actor ON film.film_id=film_actor.film_id
JOIN actor ON film_actor.actor_id=actor.actor_id
WHERE actor.actor_id=5