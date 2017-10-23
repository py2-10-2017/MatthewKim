SELECT domain_name as website, clients.client_id FROM clients
JOIN sites ON clients.client_id=sites.client_id
WHERE clients.client_id=10