select manager.emp_id,t2.name ,t1.Team_name, t1.team_id from manager
join (select team_id,team_name  from team) as t1
join (select emp_id,emp_name as name from employee)as t2 where 
t1.team_id=manager.team_id and t2.emp_id=manager.emp_id and manager.emp_id=%s;