from __future__ import print_function
import flask
from flask import request, jsonify
import re, math
from flask_cors import CORS
from random import randint
#from collections import Counter
#from google.cloud import bigquery
#from google.oauth2 import service_account
#import pandas as pd
#from pandas.io import gbq
import json
import os

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>API</h1><p>Test Api</p>"

# JD Dashboard
@app.route('/addjd', methods=['GET'])
def addjd():
               
    a= [{
"JD_Name": ".Net",
"ID":1001,
"No_of_Position":200,
"Skill_Sets":".Net",
"Created_Date":"10-8-2018",
"Received_profile":100,
"Interview_completed":50,
"Yet_to_schedule":50 
},

{
"JD_Name": "C#",
"ID":1002,
"No_of_Position":200,
"Skill_Sets":"C#",
"Created_Date":"12-8-2018",
"Received_profile":120,
"Interview_completed":50,
"Yet_to_schedule":70 
},

{
"JD_Name": "Big Data",
"ID":1003,
"No_of_Position":100,
"Skill_Sets":"Hadoop,Spark,Scala",
"Created_Date":"12-8-2018",
"Received_profile":80,
"Interview_completed":50,
"Yet_to_schedule":30 
},
{
"JD_Name": "UI Developer",
"ID":1004,
"No_of_Position":50,
"Skill_Sets":"Angular,Nodejs",
"Created_Date":"16-8-2018",
"Received_profile":40,
"Interview_completed":10,
"Yet_to_schedule":30}
]

    
    return jsonify(data = a)

# ADD New JD
@app.route('/addjobdesc', methods=['GET'])
def addjobdesc():
    a = eval(request.args['questions'])
    JD_Name = a['JD_Name']
    BU_Name = a['BU_Name']
    L0_interview  = a['L0_interview']
    L1_Panelist_1 = a['L1_Panelist_1']
    L1_Panelist_2 = a['L1_Panelist_2']
    L2_Panelist_1 = a['L2_Panelist_1']
    L1_Panelist_2 = a['L2_Panelist_2']
    Designation = a['Designation']
    Years_of_Exp = a['Years_of_Exp']
    No_of_Position = a['No_of_Position']
    Skills = a['Skills']
    Program_code = a['Program_code']
    op = randint(1005,1100)
    return jsonify(data = op)

# View Profile
@app.route('/viewjd', methods=['GET'])
def viewjd():
    a = eval(request.args['questions'])
               
    b= [{
"ID":1001,
"Name":"Sakya Maiti",
"Email":"sakya@gmail.com",
"Phone_No": 1234567890,
"Profile":"www.google.com",
"Exp":8,
"Int_Stage":"L0",
},
{
"ID":1001,
"Name":"Varun Anant",
"Email":"varun@gmail.com",
"Phone_No": 1234567890,
"Profile":"www.google.com",
"Exp":5,
"Int_Stage":"L1",
},

{
"ID":1002,
"Name":"Abhishek",
"Email":"abhi@gmail.com",
"Phone_No": 1234567890,
"Profile":"www.google.com",
"Exp":2,
"Int_Stage":"Selected",
},
{
"ID":1002,
"Name":"Kamal",
"Email":"kamal@gmail.com",
"Phone_No": 1234567890,
"Profile":"www.google.com",
"Exp":2,
"Int_Stage":"Complete",
}]
    return jsonify(data = b)
	
if __name__ == '__main__':
	import logging
	logging.basicConfig(filename='error.log',level=logging.DEBUG)
	port = int(os.getenv('PORT', 5000))
	print("Starting app on port %d" % port)
	app.run(debug=True, port=port, host='0.0.0.0')

