select status, count(status) as number_of_tickets from request_ticket group by status;