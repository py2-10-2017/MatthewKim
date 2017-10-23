SELECT concat(clients.first_name, ' ', clients.last_name) as client_name, domain_name as website, count(leads_id) as number_of_leads, date_format(registered_datetime,'%M %e, %Y') as date_generated FROM clients
JOIN sites ON clients.client_id=sites.client_id
JOIN leads ON sites.site_id=leads.site_id
WHERE year(registered_datetime)=2011
GROUP BY domain_name
ORDER BY clients.client_id