SELECT month(charged_datetime) as month, SUM(amount) as revenue FROM billing
WHERE month(charged_datetime)=3 AND year(charged_datetime)=2012