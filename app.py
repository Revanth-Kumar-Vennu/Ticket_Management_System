# Main server app

from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename
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

os.chdir(__file__.replace(basename(__file__), ''))

app = Flask(__name__)
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# MY db connection
local_server= True
# app = Flask(__name__)
app.secret_key='kusumachandashwini'


# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index(): 
    team = database.source("all_team.sql")
    print(team)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()