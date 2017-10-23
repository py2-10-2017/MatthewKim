SELECT clients.client_id, COUNT(domain_name) as number_of_websites, month(created_datetime) as month_created, year(created_datetime) as year_created FROM clients
LEFT JOIN sites ON clients.client_id=sites.client_id
WHERE clients.client_id=1
GROUP BY month(created_datetime), year(created_datetime)

SELECT clients.client_id, COUNT(domain_name) as number_of_websites, month(created_datetime) as month_created, year(created_datetime) as year_created FROM clients
LEFT JOIN sites ON clients.client_id=sites.client_id
WHERE clients.client_id=20
GROUP BY month(created_datetime), year(created_datetime)
