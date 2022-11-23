select employee.*,t.name from employee join (select team_id,team_name as name from team) as t where t.team_id=employee.team_id;
