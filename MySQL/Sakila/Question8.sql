SELECT actor.actor_id, CONCAT(first_name,' ',last_name), film.film_id, title, description, release_year, rating, special_features, name FROM film
JOIN film_actor ON film.film_id=film_actor.film_id
JOIN actor ON film_actor.actor_id=actor.actor_id
JOIN film_category ON film.film_id=film_category.film_id
JOIN category ON film_category.category_id=category.category_id
WHERE CONCAT(first_name,' ',last_name)="SANDRA KILMER" AND name="Action"