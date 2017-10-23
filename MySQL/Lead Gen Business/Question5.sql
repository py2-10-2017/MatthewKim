SELECT domain_name as website, COUNT(leads_id) as number_of_leads, date_format(registered_datetime,'%M %e, %Y') as date_generated FROM sites
JOIN leads ON sites.site_id=leads.site_id
WHERE month(registered_datetime) BETWEEN 1 and 2 AND year(registered_datetime)=2011
GROUP BY domain_name