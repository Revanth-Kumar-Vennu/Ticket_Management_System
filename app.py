# Main server app

from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename
import mysql.connector as mysql
import os
from os.path import join, dirname, realpath, basename
import database
import json
from datetime import datetime

from flask import Flask,render_template,request,session,redirect,url_for,flash
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
local_server= True
# app = Flask(__name__)
app.secret_key='kusumachandashwini'


toastr = Toastr(app)


# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/allteams')
def index1(): 
    team = database.source("all_team.sql")
    print(team)
    return render_template('teams.html')

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
    app.run()