WITH cte as(
select priority, count(priority) as number_of_tickets from incident_ticket group by priority
UNION ALL
select priority, count(priority) as number_of_tickets from request_ticket group by priority
UNION ALL
select priority, count(priority) as number_of_tickets from change_ticket group by priority)
select priority, SUM(number_of_tickets) as number_of_tickets from cte GROUP BY priority;