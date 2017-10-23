SELECT store.store_id, city.city_id, first_name, last_name, email, address FROM customer
JOIN address ON customer.address_id=address.address_id
JOIN city ON address.city_id=city.city_id
JOIN STORE ON customer.store_id=store.store_id
WHERE store.store_id=1 AND (city.city_id=1 OR city.city_id=42 OR city.city_id=312 OR city.city_id=459)