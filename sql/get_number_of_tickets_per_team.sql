WITH cte as(
select t2.team_name ,count(incident_ticket.ticket_id) as number_of_tickets from incident_ticket join
(select sprint_team.*,t1.team_name from sprint_team
join (select team_id,team_name from team) as t1 where sprint_team.team_id=t1.team_id) as t2
where incident_ticket.sprint_id=t2.sprint_id GROUP BY t2.team_name
UNION ALL
select t2.team_name ,count(request_ticket.ticket_id) as number_of_tickets from request_ticket join
(select sprint_team.*,t1.team_name from sprint_team
join (select team_id,team_name from team) as t1 where sprint_team.team_id=t1.team_id) as t2
where request_ticket.sprint_id=t2.sprint_id GROUP BY t2.team_name
UNION ALL
select t2.team_name ,count(change_ticket.ticket_id) as number_of_tickets from change_ticket join
(select sprint_team.*,t1.team_name from sprint_team
join (select team_id,team_name from team) as t1 where sprint_team.team_id=t1.team_id) as t2
where change_ticket.sprint_id=t2.sprint_id GROUP BY t2.team_name)
select cte.team_name,SUM(cte.number_of_tickets) as number_of_tickets from cte GROUP BY team_name;