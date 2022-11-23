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
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/allteams')
def index1():
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

    return render_template('teams.html', data=data, type="team", headings=headings)


@app.route('/allsprints')
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

    return render_template('teams.html', data=data, type="sprint", headings=headings)


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

    return render_template('teams.html', data=data, type="sprint", headings=headings)


@app.route('/allmanagers')
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

    return render_template('teams.html', data=data, type="manager", headings=headings)

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

    return render_template('teams.html', data=data, type="sprint", headings=headings)


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

    return render_template('teams.html', data=data, type="sprint", headings=headings)

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
            val[10],
            val[11],
            val[12],
            val[13]
           
        ]
        data.append(row)


    headings = ["ID", "Description", "Start date", "Status","Priority","Sprint Name","Team Name","Created By","Acceptor","Implementor"]

    return render_template('teams.html', data=data, type="sprint", headings=headings)

@app.route('/createteam',methods=['GET', 'POST'])
def createTeam(): 
    if request.method == 'POST':
        team_id = request.form['team_id']
        team_name = request.form['team_name']
        team_description = request.form['team_description']
        team_location = request.form['team_location']
        try:
            database.source("create_team.sql", team_id, team_name, team_description, team_location,output=False)
            return redirect(url_for('index'))
        except mysql.IntegrityError as err:
            print(err)
            flash(err, 'error')

    return render_template("create_team.html")

if __name__ == '__main__':
    app.run(debug=True)
