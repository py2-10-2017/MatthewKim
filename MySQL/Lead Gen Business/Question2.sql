SELECT clients.client_id, SUM(amount) as total_revenue FROM clients
JOIN billing ON clients.client_id=billing.client_id
WHERE clients.client_id=2