SELECT city.city_id, city, first_name, last_name, email, address FROM customer
JOIN address ON address.address_id=customer.address_id
JOIN city ON city.city_id=address.city_id
WHERE city.city_id=312
