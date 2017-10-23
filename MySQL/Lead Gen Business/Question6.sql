SELECT concat(clients.first_name,' ',clients.last_name) as client_name, count(leads_id) as number_of_leads FROM CLIENTS
JOIN sites ON clients.client_id=sites.client_id
JOIN leads ON sites.site_id=leads.site_id
WHERE year(registered_datetime)=2011
GROUP BY concat(clients.first_name,' ',clients.last_name)