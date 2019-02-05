# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:29:33 2019

@author: ottil
"""

#TASK 1: BUILD SIMPLE WEB APP

from flask import Flask, render_template, request
from search_engine import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/business")
def show_businesses():
    businesses = get_all_businesses()
    return render_template("business.html", businesses = businesses)

@app.route("/personal")
def show_people():
    people = get_all_people()
    return render_template("personal.html", people = people)


if __name__== '__main__':
    app.run(debug=True)
    
    
