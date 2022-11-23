WITH cte AS(
SELECT ticket_id, start_date FROM incident_ticket WHERE (cast(start_date as date) BETWEEN %s AND 
%s ) 
UNION
SELECT  ticket_id, start_date FROM request_ticket WHERE (cast(start_date as date) BETWEEN %s AND 
%s ) 
UNION
SELECT ticket_id, start_date FROM change_ticket WHERE (cast(start_date as date) BETWEEN %s AND 
%s )) 
SELECT start_date,COUNT(*) FROM cte GROUP BY start_date  ORDER BY start_date;