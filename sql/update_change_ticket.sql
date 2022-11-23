update change_ticket
SET 
description=%s,start_date=%s,status=%s, priority=%s,sprint_id=%s,created_by=%s,acceptor=%s,implementor=%s
where
ticket_id=%s;