from __future__ import print_function
import flask
from flask import request, jsonify
import re, math
from flask_cors import CORS
from random import randint
#from collections import Counter
#from google.cloud import bigquery
#from google.oauth2 import service_account
import pandas as pd
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
b = [ {
"Jd_Id":"1001",
"jd_Name":".Net",
"created_date":"12-02-2018",
"Profiles": [{"email":"sakya@gmail.com",
	"Exp":8,
	"Int_Stage": "L0", 
	"Name": "Sakya Maiti", 		
	"Phone_No": 1234567890, 
	"Prof_ID": 123, 
	"Profile": "www.google.com"
  		},
		{
	"email":"varun@gmail.com",
	"Exp":8,
	"Int_Stage": "Rejected", 
	"Name": "Varun Anant", 			
	"Phone_No": 1234567890, 
	"Prof_ID": 124, 
	"Profile": "www.google.com"
  		},
		{
	"email":"abi@gmail.com",
	"Exp":8,
	"Int_Stage": "Completed", 
	"Name": "Abhi Chu", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 125, 
	"Profile": "www.google.com"
  		}]
},{
"Jd_Id":"1002",
"jd_Name":"C#",
"created_date":"12-02-2018",
"Profiles": [{"email":"nishant@gmail.com",
	"Exp":8,
	"Int_Stage": "L0", 
	"Name": "Nishant", 		
	"Phone_No": 1234567890, 
	"Prof_ID": 126, 
	"Profile": "www.google.com"
  		},
		{
	"email":"shalaj@gmail.com",
	"Exp":8,
	"Int_Stage": "Rejected", 
	"Name": "Shalaj", 			
	"Phone_No": 1234567890, 
	"Prof_ID": 127, 
	"Profile": "www.google.com"
  		},
		{
	"email":"karan@gmail.com",
	"Exp":8,
	"Int_Stage": "Completed", 
	"Name": "Karan", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 128, 
	"Profile": "www.google.com"
  		}],
},{
"Jd_Id":"1003",
"jd_Name":"Big Data",
"created_date":"12-02-2018",
"Profiles": [{"email":"piyush@gmail.com",
	"Exp":8,
	"Int_Stage": "L0", 
	"Name": "piyush", 		
	"Phone_No": 1234567890, 
	"Prof_ID": 129, 
	"Profile": "www.google.com"
  		},
		{
	"email":"babu@gmail.com",
	"Exp":8,
	"Int_Stage": "Rejected", 
	"Name": "Babu", 			
	"Phone_No": 1234567890, 
	"Prof_ID": 130, 
	"Profile": "www.google.com"
  		},
		{
	"email":"vinod@gmail.com",
	"Exp":8,
	"Int_Stage": "Completed", 
	"Name": "Vinod", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 131, 
	"Profile": "www.google.com"
  		}]
},{
"Jd_Id":"1004",
"jd_Name":"UI Developer",
"created_date":"12-02-2018",
"Profiles": [{"email":"ranjan@gmail.com",
	"Exp":8,
	"Int_Stage": "L0", 
	"Name": "Ranjan", 		
	"Phone_No": 1234567890, 
	"Prof_ID": 132, 
	"Profile": "www.google.com"
  		},
		{
	"email":"rakesh@gmail.com",
	"Exp":8,
	"Int_Stage": "Rejected", 
	"Name": "Rakesh", 			
	"Phone_No": 1234567890, 
	"Prof_ID": 133, 
	"Profile": "www.google.com"
  		},
		{
	"email":"subhajit@gmail.com",
	"Exp":8,
	"Int_Stage": "Completed", 
	"Name": "Subhajit", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 134, 
	"Profile": "www.google.com"
  		}]
}] 
#print(len(b))
@app.route('/viewjd', methods=['GET'])
def viewjd():
	#a = eval(request.args['questions'])
	i = 0
	a=[]
	for i in range(0,len(b)):
		
		if b[i]["Jd_Id"] == str(request.args['questions']):
			a.append(b[i])
			
	return jsonify(data = a)

    
	
# Add new Profile
@app.route('/newprof', methods=['GET'])
def newprof():
	a = eval(request.args['questions'])
	JD_ID = a["JD_ID"]
	First_Name = a['First_Name']
	Last_Name = a['Last_Name']
	Email  = a['Email']
	Phone_No = a['Phone_No']
	op = randint(1005,1100)
	return jsonify(data = op)
	
if __name__ == '__main__':
	import logging
	logging.basicConfig(filename='error.log',level=logging.DEBUG)
	port = int(os.getenv('PORT', 5000))
	print("Starting app on port %d" % port)
	app.run(debug=True, port=port, host='0.0.0.0')
