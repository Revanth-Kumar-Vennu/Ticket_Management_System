select change_ticket.*,t1.sprint_name,t2.emp_name as created_by,t3.team_name,t4.emp_name as acceptor_name,t5.emp_name as implementor_name from change_ticket
join 
(select sprint_id,sprint_name from sprint) as t1
join (select emp_name,emp_id from employee) as t2
join (select sprint_team.team_id as team_id, sprint_team.sprint_id as sprint_id, t.team_name as team_name from sprint_team
join (select team_name,team_id from team) as t where t.team_id=sprint_team.team_id) as t3
join (select emp_name,emp_id from employee) as t4
join (select emp_name,emp_id from employee) as t5
where t1.sprint_id=change_ticket.sprint_id and t2.emp_id=change_ticket.created_by and t3.sprint_id=change_ticket.sprint_id
and t4.emp_id=change_ticket.acceptor and t5.emp_id=change_ticket.implementor;