SELECT film.film_id, title, actor.actor_id, CONCAT(first_name,' ',last_name) as actor_name FROM film
JOIN film_actor ON film.film_id=film_actor.film_id
JOIN actor ON film_actor.actor_id=actor.actor_id
WHERE film.film_id=369