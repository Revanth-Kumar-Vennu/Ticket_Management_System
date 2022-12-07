# Main server app

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mysql
import os
from os.path import join, dirname, realpath, basename
import database

from flask import Flask, render_template, request, redirect, url_for, flash
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
    team = database.sourceProc("getAllTeams")
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
    team = database.sourceProc("getAllSprints")
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
    team = database.sourceProc("getAllEmployees")
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
    employees = database.sourceProc("getAllEmployees")
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
    team = database.sourceProc("getAllManagers")
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
    team = database.sourceProc("getAllIncidents")
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
    team = database.sourceProc("getAllRequests")
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
    team = database.sourceProc("getAllChanges")
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
        # team_id = request.form['team_id']
        team_name = request.form['team_name']
        team_description = request.form['team_description']
        team_location = request.form['team_location']
        try:
            # database.source("create_team.sql", team_name, team_description, team_location,output=False)
            database.sourceProc("createTeam", team_name, team_description, team_location,output=False)
            return redirect(url_for('allTeams'))
            
        except Exception as err:
            flash(err, 'error')

    return render_template("create_team.html")

@app.route('/createIncident',methods=['GET', 'POST'])
def createIncident(): 
    sprints = database.sourceProc("getAllSprints")
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
            database.sourceProc("createIncident", inc_id, inc_description, inc_start, inc_status,inc_priority,inc_sprint,inc_created,output=False)
            return redirect(url_for('incidents'))
        except Exception as err:
            error=str(err)
            if 'incident_ticket.PRIMARY' in error:
                flash("Provided Incident ID already exists, please provide another Incident ID", 'error')
            else:
                flash(err, 'error')
    return render_template("create_incident.html", data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))


@app.route('/createRequest',methods=['GET', 'POST'])
def createRequest(): 
    sprints = database.sourceProc("getAllSprints")
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
            database.sourceProc("createRequest", req_id, req_description, req_start, req_status,req_priority,req_sprint,req_created,output=False)
            return redirect(url_for('requests'))
        except Exception as err:
            error=str(err)
            if 'request_ticket.PRIMARY' in error:
                flash("Provided Request ID already exists, please provide another Request ID", 'error')
            else:
                flash(err, 'error')

    return render_template("create_request.html", data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))


@app.route('/createChange',methods=['GET', 'POST'])
def createChange(): 
    sprints = database.sourceProc("getAllSprints")
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
            database.sourceProc("createChange", chg_id, chg_description, chg_start, chg_status,chg_priority,chg_sprint,chg_created,chg_acceptor,chg_implementor,output=False)
            return redirect(url_for('changes'))
        except Exception as err:
            error=str(err)
            if 'change_ticket.PRIMARY' in error:
                flash("Provided Change ID already exists, please provide another Change ID", 'error')
            else:
                flash(err, 'error')

    return render_template("create_change.html", data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))

@app.route('/createSprint',methods=['GET', 'POST'])
def createSprint(): 
    team = database.sourceProc("getAllTeams")
    data = []
    for val in team:
        row = [
            val[0],
            val[1]
        ]
        data.append(row)
    if request.method == 'POST':
        # sprint_id = request.form['sprint_id']
        sprint_name = request.form['sprint_name']
        sprint_start = request.form['sprint_start']
        sprint_end = request.form['sprint_end']
        sprint_team = request.form['sprint_team']
        try:
            database.sourceProc("createSprint", sprint_name, sprint_start, sprint_end,output=False)
            sprint_id=database.sourceProc("getLatestSprintID")
            database.sourceProc("createSprintTeam", sprint_id[0][0], sprint_team,output=False)
            return redirect(url_for('sprints'))
        except Exception as err:
            
            flash(err, 'error')

    return render_template("create_sprint.html", data=data, len_team=len(data))

@app.route('/createEmployee',methods=['GET', 'POST'])
def createEmployee(): 
    team = database.sourceProc("getAllTeams")
    data = []
    for val in team:
        row = [
            val[0],
            val[1]
        ]
        data.append(row)
    if request.method == 'POST':
        # emp_id = request.form['emp_id']
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
            database.sourceProc("createEmployee",team_id,emp_name,date_of_birth,sex,address_street_name,address_street_number,address_zipcode,address_city,address_state,phone_number,joining_date,output=False)
            return redirect(url_for('employees'))
        except Exception as err:
            
            flash(err, 'error')

    return render_template("create_employee.html", data=data, len_team=len(data))

@app.route('/createManager',methods=['GET', 'POST'])
def createManager(): 
    team = database.sourceProc("getAllTeams")
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
            database.sourceProc("createManager", emp_id,team_id,output=False)
            return redirect(url_for('managers'))
        except Exception as err:
            error=str(err)
            print(error)
            if "manager.PRIMARY" in error:
                flash("The manager that you have selected already manages a team, please select a different manager or edit the manager if you wish you change the team.", 'error')
            elif "manager.team_id_UNIQUE" in error:
                flash("Team that you provided already has a manager!",'error')
            else:
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
            database.sourceProc("updateTeam", team_name, team_description, team_location,team_id,output=False)
            return redirect(url_for('allTeams'))
        except Exception as err:
            
            flash(err, 'error')
    
    values=database.sourceProc("getTeam",id)

    return render_template("edit_team.html",values=values,id=id)

@app.route('/delete/Incidents/<id>',methods=['GET', 'POST'])
def deleteTeam(id): 
    try:
        database.sourceProc("deleteIncident",id,output=False)
    except Exception as err:
        
        flash(err, 'error')
    return redirect(url_for('incidents'))

@app.route('/delete/Requests/<id>',methods=['GET', 'POST'])
def deleteRequest(id): 
    try:
        database.sourceProc("deleteRequest",id,output=False)
    except Exception as err:
        
        flash(err, 'error')
    return redirect(url_for('requests'))

@app.route('/delete/Changes/<id>',methods=['GET', 'POST'])
def deleteChange(id): 
    try:
        database.sourceProc("deleteChange",id,output=False)
    except Exception as err:
        
        flash(err, 'error')
    return redirect(url_for('changes'))

@app.route('/delete/Managers/<id>',methods=['GET', 'POST'])
def deleteManager(id): 
    try:
        database.sourceProc("deleteManager",id,output=False)
    except Exception as err:
        flash(err, 'error')
    return redirect(url_for('managers'))
    
@app.route('/edit/Employees/<id>',methods=['GET', 'POST'])
def editEmployee(id): 
    team = database.sourceProc("getAllTeams")
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
            database.sourceProc("updateEmployee",team_id,emp_name,date_of_birth,sex,address_street_name,address_street_number,address_zipcode,address_city,address_state,phone_number,joining_date,emp_id,output=False)
            return redirect(url_for('employees'))
        except Exception as err:
            
            flash(err, 'error')
    
    values=database.sourceProc("getEmployee",id)
    return render_template("edit_employee.html",values=values,id=id, data=data,len_team=len(data))

@app.route('/edit/Sprints/<id>',methods=['GET', 'POST'])
def editSprint(id): 
    team = database.sourceProc("getAllTeams")
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
            database.sourceProc("updateSprint",  sprint_name, sprint_start, sprint_end,sprint_id,output=False)
            database.sourceProc("updateSprintTeam",  sprint_team,sprint_id,output=False)
            return redirect(url_for('sprints'))
        except Exception as err:
            
            flash(err, 'error')
    values=database.sourceProc("getSprint",id)


    return render_template("edit_sprint.html", values=values,data=data, len_team=len(data),id=id)

@app.route('/edit/Managers/<id>',methods=['GET', 'POST'])
def editManager(id): 
    team = database.sourceProc("getAllTeams")
    data = []
    for val in team:
        row = [
            val[0],
            val[1]
        ]
        data.append(row)
    employees = getEmployeeIdAndName()
    if request.method == 'POST':
        team_id = request.form['team_id']
        try:
            database.sourceProc("updateManager",team_id,id,output=False)
            return redirect(url_for('managers'))
        except Exception as err:
            error=str(err)
            print(error)
            if "manager.team_id_UNIQUE" in error:
                flash("The team that you provided already has a manager",'error')
            else:
                print(error)
                flash(err, 'error')
    values=database.sourceProc("getManager",id)


    return render_template("edit_manager.html", data=data, values=values,id=id,len_team=len(data))


@app.route('/edit/Incidents/<id>',methods=['GET', 'POST'])
def editIncident(id): 
    sprints = database.sourceProc("getAllSprints")
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
            database.sourceProc("updateIncident", inc_description, inc_start, inc_status,inc_priority,inc_sprint,inc_created,id,output=False)
            return redirect(url_for('incidents'))
        except Exception as err:
            
            flash(err, 'error')
    values=database.sourceProc("getIncident",id)
  

    return render_template("edit_incident.html",id=id, values=values,data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))

@app.route('/edit/Requests/<id>',methods=['GET', 'POST'])
def editRequest(id): 
    sprints = database.sourceProc("getAllSprints")
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
            database.sourceProc("updateRequest", req_description, req_start, req_status,req_priority,req_sprint,req_created,id,output=False)
            return redirect(url_for('requests'))
        except Exception as err:
            
            flash(err, 'error')
    values=database.sourceProc("getRequest",id)

    return render_template("edit_request.html",id=id, values=values,data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))


@app.route('/edit/Changes/<id>',methods=['GET', 'POST'])
def editChange(id): 
    sprints = database.sourceProc("getAllSprints")
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
            database.sourceProc("updateChange",chg_description, chg_start, chg_status,chg_priority,chg_sprint,chg_created,chg_acceptor,chg_implementor,id,output=False)
            return redirect(url_for('changes'))
        except Exception as err:
            
            flash(err, 'error')
    values=database.sourceProc("getChange",id)


    return render_template("edit_change.html",id=id, values=values,data=data, len_sprint=len(data),employees=employees,len_employee=len(employees))

@app.route('/getChart',methods=['GET', 'POST'])
def renderChart():
    data = []
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        tickets = database.sourceProc("getTicketsBetweenDates",start_date,end_date)
        for val in tickets:
            row = [
                str(val[0]),
                val[1],
            ]
            data.append(row)
    return render_template('render_chart.html',data=data)

@app.route('/getDataInsights',methods=['GET', 'POST'])
def renderChartInsights():
    inc_data = []
    req_data=[]
    chg_data=[]
    incident_tickets = database.sourceProc("getIncidentStatus")
    request_tickets = database.sourceProc("getRequestStatus")
    change_tickets=database.sourceProc("getChangeStatus")
    for val in incident_tickets:
        row = [
                str(val[0]),
                val[1],
            ]
        inc_data.append(row)

    for val in request_tickets:
        row = [
                str(val[0]),
                val[1],
            ]
        req_data.append(row)

    for val in change_tickets:
        row = [
                str(val[0]),
                val[1],
            ]
        chg_data.append(row)

    number_of_tickets_per_team=database.sourceProc('getNumberOfTickersPerTeam')
    number_of_tickets_per_priority=database.sourceProc("getTicketsByPriority")
 

    return render_template('charts.html',inc_data=inc_data,req_data=req_data,chg_data=chg_data,number_of_tickets_per_team=number_of_tickets_per_team,number_of_tickets_per_priority=number_of_tickets_per_priority)

if __name__ == '__main__':
    app.run(debug=True)
