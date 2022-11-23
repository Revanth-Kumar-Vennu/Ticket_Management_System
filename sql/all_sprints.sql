select sprint.*,t1.team_name from sprint join
(select sprint_team.team_id as team_id, sprint_team.sprint_id as sprint_id, t.team_name as team_name from sprint_team
join (select team_name,team_id from team) as t where t.team_id=sprint_team.team_id) 
as t1 where sprint.sprint_id=t1.sprint_id;