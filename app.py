# Main server app

from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename
import mysql.connector as mysql
import os
from os.path import join, dirname, realpath, basename
import database
import json
from datetime import datetime

from flask import Flask, render_template, request, session, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from flask_toastr import Toastr


os.chdir(__file__.replace(basename(__file__), ''))

app = Flask(__name__)
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# MY db connection
local_server = True
# app = Flask(__name__)
app.secret_key = 'kusumachandashwini'


toastr = Toastr(app)


# this is for getting unique user access
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/allTeams')
def allTeams():
    team = database.source("all_team.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1],
            val[2],
            val[3]
        ]
        data.append(row)
    headings = ["ID", "Team Name", "Description", "Location"]

    return render_template('teams.html', data=data, type="Teams",name="Team", headings=headings)


@app.route('/allSprints')
def sprints():
    team = database.source("all_sprints.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1],
            val[4],
            val[2].strftime("%b %d, %Y"),
            val[3].strftime("%b %d, %Y")
        ]
        data.append(row)
    headings = ["ID", "Sprint Name", "Team name","Start Date", "End Date"]

    return render_template('teams.html', data=data, type="Sprints",name="Sprint", headings=headings)


@app.route('/allEmployees')
def employees():
    team = database.source("all_employees.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[12],
            val[2],
            val[3].strftime("%b %d, %Y"),
            val[4],
            val[6] +" "+ 
            val[5] +", "+ 
            val[8] +", "+ 
            val[9] +", "+ 
            val[7],
            val[10],
            val[11].strftime("%b %d, %Y")
        ]
        data.append(row)

    headings = ["ID", "Team Name", "Name", "Date Of Birth","Sex","Address","Phone Number","Joining Date"]

    return render_template('teams.html', data=data, type="Employees",name="Employee", headings=headings)

def getEmployeeIdAndName():
    employees = database.source("all_employees.sql")
    data = []
    for val in employees:
        row = [
            val[0],
            val[2]
        ]
        data.append(row)
    return data

@app.route('/allManagers')
def managers():
    team = database.source("all_managers.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1],
            val[2]
        ]
        data.append(row)
    headings = ["ID","Manager Name", "Team Name"]

    return render_template('teams.html', data=data, type="Managers",name="Manager", headings=headings)

@app.route('/allIncidents')
def incidents():
    team = database.source("all_incident_ticket.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1],
            val[2].strftime("%b %d, %Y"),
            val[3],
            val[4],
            val[7],
            val[9],
            val[8]
           
        ]
        data.append(row)


    headings = ["ID", "Description", "Start date", "Status","Priority","Sprint Name","Team Name","Created By"]

    return render_template('teams.html', data=data, type="Incidents", name="Incident",headings=headings)


@app.route('/allRequests')
def requests():
    team = database.source("all_requests_tickets.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1],
            val[2].strftime("%b %d, %Y"),
            val[3],
            val[4],
            val[7],
            val[9],
            val[8]
           
        ]
        data.append(row)


    headings = ["ID", "Description", "Start date", "Status","Priority","Sprint Name","Team Name","Created By"]

    return render_template('teams.html', data=data, type="Requests", name="Request",headings=headings)

@app.route('/allChanges')
def changes():
    team = database.source("all_change_tickets.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1],
            val[2].strftime("%b %d, %Y"),
            val[3],
            val[4],
            val[9],
            val[11],
            val[10],
            val[12],
            val[13]
           
        ]
        data.append(row)


    headings = ["ID", "Description", "Start date", "Status","Priority","Sprint Name","Team Name","Created By","Acceptor","Implementor"]

    return render_template('teams.html', data=data, type="Changes", name="Change", headings=headings)

@app.route('/createTeam',methods=['GET', 'POST'])
def createTeam(): 
    if request.method == 'POST':
        team_id = request.form['team_id']
        team_name = request.form['team_name']
        team_description = request.form['team_description']
        team_location = request.form['team_location']
        try:
            database.source("create_team.sql", team_id, team_name, team_description, team_location,output=False)
            return redirect(url_for('index'))
        except Exception as err:
            print(err)
            flash(err, 'error')

    return render_template("create_team.html")

@app.route('/createIncident',methods=['GET', 'POST'])
def createIncident(): 
    sprints = database.source("all_sprints.sql")
    data = []
    for val in sprints:
        row = [
            val[0],
            val[1],
        ]
        data.append(row)
    employees = getEmployeeIdAndName()
    if request.method == 'POST':
        inc_id = request.form['inc_id']
        inc_description = request.form['inc_description']
        inc_start = request.form['inc_start']
        inc_status = request.form['inc_status']
        inc_priority = request.form['inc_priority']
        inc_sprint = request.form['inc_sprint']
        inc_created = request.form['inc_created']
        try:
            database.source("create_incident_ticket.sql", inc_id, inc_description, inc_start, inc_status,inc_priority,inc_sprint,inc_created,output=False)
            return redirect(url_for('index'))
        except Exception as err:
            print(err)
            flash(err, 'error')

    return render_template("create_incident.html", data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))


@app.route('/createRequest',methods=['GET', 'POST'])
def createRequest(): 
    sprints = database.source("all_sprints.sql")
    data = []
    for val in sprints:
        row = [
            val[0],
            val[1],
        ]
        data.append(row)
    employees = getEmployeeIdAndName()
    if request.method == 'POST':
        req_id = request.form['req_id']
        req_description = request.form['req_description']
        req_start = request.form['req_start']
        req_status = request.form['req_status']
        req_priority = request.form['req_priority']
        req_sprint = request.form['req_sprint']
        req_created = request.form['req_created']
        try:
            database.source("create_request_ticket.sql", req_id, req_description, req_start, req_status,req_priority,req_sprint,req_created,output=False)
            return redirect(url_for('index'))
        except Exception as err:
            print(err)
            flash(err, 'error')

    return render_template("create_request.html", data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))


@app.route('/createChange',methods=['GET', 'POST'])
def createChange(): 
    sprints = database.source("all_sprints.sql")
    data = []
    for val in sprints:
        row = [
            val[0],
            val[1],
        ]
        data.append(row)
    employees = getEmployeeIdAndName()
    if request.method == 'POST':
        chg_id = request.form['chg_id']
        chg_description = request.form['chg_description']
        chg_start = request.form['chg_start']
        chg_status = request.form['chg_status']
        chg_priority = request.form['chg_priority']
        chg_sprint = request.form['chg_sprint']
        chg_created = request.form['chg_created']
        chg_acceptor = request.form['chg_acceptor']
        chg_implementor = request.form['chg_implementor']
        try:
            database.source("create_change_ticket.sql", chg_id, chg_description, chg_start, chg_status,chg_priority,chg_sprint,chg_created,chg_acceptor,chg_implementor,output=False)
            return redirect(url_for('index'))
        except Exception as err:
            print(err)
            flash(err, 'error')

    return render_template("create_change.html", data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))

@app.route('/createSprint',methods=['GET', 'POST'])
def createSprint(): 
    team = database.source("all_team.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1]
        ]
        data.append(row)
    if request.method == 'POST':
        sprint_id = request.form['sprint_id']
        sprint_name = request.form['sprint_name']
        sprint_start = request.form['sprint_start']
        sprint_end = request.form['sprint_end']
        sprint_team = request.form['sprint_team']
        try:
            database.source("create_sprint.sql", sprint_id, sprint_name, sprint_start, sprint_end,output=False)
            database.source("create_sprint_team.sql", sprint_id, sprint_team,output=False)
            return redirect(url_for('index'))
        except Exception as err:
            print(err)
            flash(err, 'error')

    return render_template("create_sprint.html", data=data, len_team=len(data))

@app.route('/createEmployee',methods=['GET', 'POST'])
def createEmployee(): 
    team = database.source("all_team.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1]
        ]
        data.append(row)
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        team_id = request.form['team_id']
        emp_name = request.form['emp_name']
        date_of_birth = request.form['date_of_birth']
        sex = request.form['sex']
        address_street_name = request.form['address_street_name']
        address_street_number = request.form['address_street_number']
        address_zipcode = request.form['address_zipcode']
        address_city = request.form['address_city']
        address_state = request.form['address_state']
        phone_number = request.form['phone_number']
        joining_date = request.form['joining_date']
        try:
            database.source("create_employee.sql", emp_id,team_id,emp_name,date_of_birth,sex,address_street_name,address_street_number,address_zipcode,address_city,address_state,phone_number,joining_date,output=False)
            return redirect(url_for('index'))
        except Exception as err:
            print(err)
            flash(err, 'error')

    return render_template("create_employee.html", data=data, len_team=len(data))

@app.route('/createManager',methods=['GET', 'POST'])
def createManager(): 
    team = database.source("all_team.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1]
        ]
        data.append(row)
    employees = getEmployeeIdAndName()
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        team_id = request.form['team_id']
        try:
            database.source("create_manager.sql", emp_id,team_id,output=False)

            return redirect(url_for('index'))
        except Exception as err:
            print(err)
            flash(err, 'error')

    return render_template("create_manager.html", data=data, len_team=len(data),employees=employees,len_employee=len(employees))


@app.route('/edit/Teams/<id>',methods=['GET', 'POST'])
def editTeam(id): 
    if request.method == 'POST':
        team_id = request.form['team_id']
        team_name = request.form['team_name']
        team_description = request.form['team_description']
        team_location = request.form['team_location']
        try:
            database.source("update_team.sql", team_name, team_description, team_location,team_id,output=False)
            return redirect(url_for('allTeams'))
        except Exception as err:
            print(err)
            flash(err, 'error')
    
    values=database.source("getTeam.sql",id)

    print(values)
    return render_template("edit_team.html",values=values,id=id)

@app.route('/edit/Employees/<id>',methods=['GET', 'POST'])
def editEmployee(id): 
    team = database.source("all_team.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1]
        ]
        data.append(row)
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        team_id = request.form['team_id']
        emp_name = request.form['emp_name']
        date_of_birth = request.form['date_of_birth']
        sex = request.form['sex']
        address_street_name = request.form['address_street_name']
        address_street_number = request.form['address_street_number']
        address_zipcode = request.form['address_zipcode']
        address_city = request.form['address_city']
        address_state = request.form['address_state']
        phone_number = request.form['phone_number']
        joining_date = request.form['joining_date']
        try:
            database.source("update_employee.sql",team_id,emp_name,date_of_birth,sex,address_street_name,address_street_number,address_zipcode,address_city,address_state,phone_number,joining_date,emp_id,output=False)
            return redirect(url_for('employees'))
        except Exception as err:
            print(err)
            flash(err, 'error')
    
    values=database.source("get_Employee.sql",id)
    print(values)
    return render_template("edit_employee.html",values=values,id=id, data=data,len_team=len(data))

@app.route('/edit/Sprints/<id>',methods=['GET', 'POST'])
def editSprint(id): 
    team = database.source("all_team.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1]
        ]
        data.append(row)
    if request.method == 'POST':
        sprint_id = request.form['sprint_id']
        sprint_name = request.form['sprint_name']
        sprint_start = request.form['sprint_start']
        sprint_end = request.form['sprint_end']
        sprint_team = request.form['sprint_team']
        try:
            database.source("update_sprint.sql",  sprint_name, sprint_start, sprint_end,sprint_id,output=False)
            database.source("update_sprint_team.sql",  sprint_team,sprint_id,output=False)
            return redirect(url_for('sprints'))
        except Exception as err:
            print(err)
            flash(err, 'error')
    values=database.source("get_Sprint.sql",id)
    print(values)

    return render_template("edit_sprint.html", values=values,data=data, len_team=len(data),id=id)

@app.route('/edit/Managers/<id>',methods=['GET', 'POST'])
def editManager(id): 
    team = database.source("all_team.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1]
        ]
        data.append(row)
    print(data)
    employees = getEmployeeIdAndName()
    if request.method == 'POST':
        team_id = request.form['team_id']
        try:
            database.source("update_managers.sql",team_id,id,output=False)

            return redirect(url_for('managers'))
        except Exception as err:
            print(err)
            flash(err, 'error')
    values=database.source("get_Manager.sql",id)
    print(values)

    return render_template("edit_manager.html", data=data, values=values,id=id,len_team=len(data))


@app.route('/edit/Incidents/<id>',methods=['GET', 'POST'])
def editIncident(id): 
    sprints = database.source("all_sprints.sql")
    data = []
    for val in sprints:
        row = [
            val[0],
            val[1],
        ]
        data.append(row)
    employees = getEmployeeIdAndName()
    if request.method == 'POST':
        inc_id = request.form['inc_id']
        inc_description = request.form['inc_description']
        inc_start = request.form['inc_start']
        inc_status = request.form['inc_status']
        inc_priority = request.form['inc_priority']
        inc_sprint = request.form['inc_sprint']
        inc_created = request.form['inc_created']
        try:
            database.source("update_incident_ticket.sql", inc_description, inc_start, inc_status,inc_priority,inc_sprint,inc_created,id,output=False)
            return redirect(url_for('incidents'))
        except Exception as err:
            print(err)
            flash(err, 'error')
    values=database.source("get_Incident.sql",id)
    print(values)

    return render_template("edit_incident.html",id=id, values=values,data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))

@app.route('/edit/Requests/<id>',methods=['GET', 'POST'])
def editRequest(id): 
    sprints = database.source("all_sprints.sql")
    data = []
    for val in sprints:
        row = [
            val[0],
            val[1],
        ]
        data.append(row)
    employees = getEmployeeIdAndName()
    if request.method == 'POST':
        req_description = request.form['req_description']
        req_start = request.form['req_start']
        req_status = request.form['req_status']
        req_priority = request.form['req_priority']
        req_sprint = request.form['req_sprint']
        req_created = request.form['req_created']
        try:
            database.source("update_request_ticket.sql", req_description, req_start, req_status,req_priority,req_sprint,req_created,id,output=False)
            return redirect(url_for('requests'))
        except Exception as err:
            print(err)
            flash(err, 'error')
    values=database.source("get_Request.sql",id)
    print(values)

    return render_template("edit_request.html",id=id, values=values,data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))


@app.route('/edit/Changes/<id>',methods=['GET', 'POST'])
def editChange(id): 
    sprints = database.source("all_sprints.sql")
    data = []
    for val in sprints:
        row = [
            val[0],
            val[1],
        ]
        data.append(row)
    employees = getEmployeeIdAndName()
    if request.method == 'POST':
        chg_description = request.form['chg_description']
        chg_start = request.form['chg_start']
        chg_status = request.form['chg_status']
        chg_priority = request.form['chg_priority']
        chg_sprint = request.form['chg_sprint']
        chg_created = request.form['chg_created']
        chg_acceptor = request.form['chg_acceptor']
        chg_implementor = request.form['chg_implementor']
        try:
            database.source("update_change_ticket.sql",chg_description, chg_start, chg_status,chg_priority,chg_sprint,chg_created,chg_acceptor,chg_implementor,id,output=False)
            return redirect(url_for('changes'))
        except Exception as err:
            print(err)
            flash(err, 'error')
    values=database.source("get_Change.sql",id)
    print(values)

    return render_template("edit_change.html",id=id, values=values,data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))



if __name__ == '__main__':
    app.run(debug=True)
