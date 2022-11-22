CREATE DATABASE IF NOT EXISTS ticketmanagementsystem;

USE ticketmanagementsystem;

CREATE TABLE IF NOT EXISTS team (
team_id INT PRIMARY KEY,
team_name VARCHAR(20) NOT NULL,
description VARCHAR(255),
location VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS employee (
emp_id INT PRIMARY KEY,
team_id INT NOT NULL,
emp_name VARCHAR(20) NOT NULL,
date_of_birth DATE NOT NULL,
sex ENUM('Male','Female','Other'),
address_street_name VARCHAR(20),
address_street_number VARCHAR(20),
address_zipcode VARCHAR(20),
address_city VARCHAR(20),
address_state VARCHAR(20),
phone_number VARCHAR(15),
joining_date DATE,
CONSTRAINT fk_employee_team FOREIGN KEY (team_id)  REFERENCES team (team_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS manager (
emp_id INT NOT NULL,
team_id INT NOT NULL,
CONSTRAINT fk_manager_team FOREIGN KEY (team_id)  REFERENCES team (team_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT fk_manager_employee FOREIGN KEY (emp_id)  REFERENCES employee (emp_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT pk_manager PRIMARY KEY (emp_id,team_id)
);

CREATE TABLE IF NOT EXISTS sprint (
sprint_id INT PRIMARY KEY,
sprint_name VARCHAR(20) NOT NULL,
start_date DATE,
end_date DATE
);

CREATE TABLE IF NOT EXISTS sprint_team (
sprint_id INT NOT NULL,
team_id INT NOT NULL,
CONSTRAINT fk_sprint FOREIGN KEY (sprint_id)  REFERENCES sprint (sprint_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT fk_team FOREIGN KEY (team_id)  REFERENCES team (team_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT pk_sprint_team PRIMARY KEY (sprint_id,team_id)
);

CREATE TABLE IF NOT EXISTS incident_ticket (
ticket_id INT PRIMARY KEY,
description VARCHAR(20) NOT NULL,
start_date DATE NOT NULL,
status ENUM('Open','In Progress','Closed'),
priority ENUM('P1','P2','P3','P4'),
sprint_id INT NOT NULL,
created_by INT NOT NULL,
CONSTRAINT fk_incident_sprint FOREIGN KEY (sprint_id)  REFERENCES sprint (sprint_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT fk_incident_emp FOREIGN KEY (created_by)  REFERENCES employee (emp_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS request_ticket (
ticket_id INT PRIMARY KEY,
description VARCHAR(20) NOT NULL,
start_date DATE NOT NULL,
status ENUM('Open','In Progress','Closed'),
priority ENUM('P1','P2','P3','P4'),
sprint_id INT NOT NULL,
created_by INT NOT NULL,
CONSTRAINT fk_request_sprint FOREIGN KEY (sprint_id)  REFERENCES sprint (sprint_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT fk_request_emp FOREIGN KEY (created_by)  REFERENCES employee (emp_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS change_ticket (
ticket_id INT PRIMARY KEY,
description VARCHAR(20) NOT NULL,
start_date DATE NOT NULL,
status ENUM('Open','In Progress','Closed'),
priority ENUM('P1','P2','P3','P4'),
sprint_id INT NOT NULL,
created_by INT NOT NULL,
acceptor INT NOT NULL,
implementor INT NOT NULL,
CONSTRAINT fk_change_sprint FOREIGN KEY (sprint_id)  REFERENCES sprint (sprint_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT fk_change_emp FOREIGN KEY (created_by)  REFERENCES employee (emp_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT fk_change_emp_accept FOREIGN KEY (acceptor)  REFERENCES employee (emp_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT fk_change_emp_implement FOREIGN KEY (implementor)  REFERENCES employee (emp_id) ON DELETE CASCADE ON UPDATE CASCADE
);

