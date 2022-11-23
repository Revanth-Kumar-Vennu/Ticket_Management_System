# Main server app

from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath, basename
import database
import json
from datetime import datetime

from flask import Flask, render_template, request, session, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_manager, LoginManager
from flask_login import login_required, current_user

os.chdir(__file__.replace(basename(__file__), ''))

app = Flask(__name__)
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# MY db connection
local_server = True
# app = Flask(__name__)
app.secret_key = 'kusumachandashwini'


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
            val[2],
            val[3]
        ]
        data.append(row)
    headings = ["ID", "Sprint Name", "Start Date", "End Date"]

    return render_template('teams.html', data=data, type="sprint", headings=headings)


@app.route('/allEmployees')
def employees():
    team = database.source("all_employees.sql")
    data = []
    for val in team:
        row = [
            val[0],
            val[1],
            val[2],
            val[3],
            val[4],
            val[6] +" "+ 
            val[5] +", "+ 
            val[7] +", "+ 
            val[8] +", "+ 
            val[9],
            val[10],
            val[11]
        ]
        data.append(row)

    headings = ["ID", "Team ID", "Name", "Date Of Birth","Sex","Address","Phone Number","Joining Date"]

    return render_template('teams.html', data=data, type="sprint", headings=headings)


if __name__ == '__main__':
    app.run(debug=True)
