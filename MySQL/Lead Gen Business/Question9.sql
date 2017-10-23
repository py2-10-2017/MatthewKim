SELECT concat(first_name, ' ',last_name) as client_name, SUM(amount) as Total_Revenue, month(charged_datetime) as month_charge, year(charged_datetime) as year_charge FROM clients
JOIN billing ON clients.client_id=billing.client_id
GROUP BY  date_format(charged_datetime,'%m%y'), client_name
ORDER BY clients.client_id, charged_datetime