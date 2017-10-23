SELECT concat(first_name, ' ' , last_name) as client_name, group_concat(domain_name,' / ') as sites from clients
	LEFT JOIN sites ON clients.client_id=sites.client_id
group by clients.client_id