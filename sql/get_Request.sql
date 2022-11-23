select request_ticket.*,t1.sprint_name,t2.emp_name,t3.team_name from request_ticket
join 
(select sprint_id,sprint_name from sprint) as t1
join (select emp_name,emp_id from employee) as t2
join (select sprint_team.team_id as team_id, sprint_team.sprint_id as sprint_id, t.team_name as team_name from sprint_team
join (select team_name,team_id from team) as t where t.team_id=sprint_team.team_id) as t3
where t1.sprint_id=request_ticket.sprint_id and t2.emp_id=request_ticket.created_by and t3.sprint_id=request_ticket.sprint_id and request_ticket.ticket_id=%s;