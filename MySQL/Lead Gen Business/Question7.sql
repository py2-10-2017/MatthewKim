SELECT concat(clients.first_name,' ',clients.last_name) as client_name, count(leads_id) as number_of_leads, month(registered_datetime) as month_generated FROM CLIENTS
JOIN sites ON clients.client_id=sites.client_id
JOIN leads ON sites.site_id=leads.site_id
WHERE year(registered_datetime)=2011 AND month(registered_datetime) BETWEEN 1 and 6
GROUP BY concat(clients.first_name,' ',clients.last_name), month(registered_datetime)
ORDER BY month(registered_datetime)