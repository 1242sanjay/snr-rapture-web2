# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:18:25 2021

@author: Sanjay Kumar
"""


from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/myblog"
db = SQLAlchemy(app)


class Signup(db.Model):
    '''
        sno, name, email, password, date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20))

class Aipost(db.Model):
    '''
        sno, subject, title, content, date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12))
    image = db.Column(db.String(12), nullable=False)
    
    
class Cloudpost(db.Model):
    '''
        sno, subject, title, content, date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12))
    image = db.Column(db.String(12), nullable=False)
    
    
    
class Webpost(db.Model):
    '''
        sno, subject, title, content, date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12))
    image = db.Column(db.String(12), nullable=False)



@app.route("/")
def home():
    ai_post = Aipost.query.filter_by().all()[0:2]
    cloud_post = Cloudpost.query.filter_by().all()[0:2]
    web_post = Webpost.query.filter_by().all()[0:2]
    return render_template("index.html", params=params, ai_post=ai_post, cloud_post=cloud_post, web_post=web_post)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        entry = Signup(name=name, email=email, password=password, date=datetime.now())
        
        db.session.add(entry)
        db.session.commit()
        return redirect("/")
        
    return render_template("signup.html", params=params)
    
@app.route("/login")
def login():
    return render_template("login.html", params=params)


@app.route("/subscribe")
def subscribe():
    return render_template("subscribe.html", params=params)


@app.route("/aipost/<string:ai_slug>", methods=["GET"])
def aipost(ai_slug):
    ai_post = Aipost.query.filter_by(slug=ai_slug).first()  
    ai_title = Aipost.query.filter_by().all()
    return render_template("aipost.html", params=params, ai_post=ai_post, ai_title=ai_title)


@app.route("/cloudpost/<string:cloud_slug>", methods=["GET"])
def cloudpost(cloud_slug):
    cloud_post = Cloudpost.query.filter_by(slug=cloud_slug).first() 
    cloud_title = Cloudpost.query.filter_by().all()
    return render_template("cloudpost.html", params=params, cloud_post=cloud_post, cloud_title=cloud_title)


@app.route("/webpost/<string:web_slug>", methods=["GET"])
def webpost(web_slug):
    web_post = Webpost.query.filter_by(slug=web_slug).first() 
    web_title = Webpost.query.filter_by().all()
    return render_template("webpost.html", params=params, web_post=web_post, web_title=web_title)

app.run(debug=True, use_reloader=False)