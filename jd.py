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

@app.route('/authenticate', methods=['Get'])
def authenticate():
	a = eval(request.args['questions'])
	id = a["id"]
	pwd = a["pwd"]
	if (id == "ta@csscorp.com" and pwd == "pass123"):
		b = [{"login":1, "sid" : 1001, "role" : "TA"}]
	else:
		b = [{"login":0, "sid" : 0, "role" : ""}]
	return jsonify(data= b)

# JD Dashboard
@app.route('/addjd', methods=['GET'])
def addjd():
               
    a= [
	{
"JD_Name": "Apple Data Engineer",
"ID":1005,
"No_of_Position":50,
"Skill_Sets":"Big Data, Python, Hadoop, MapReduce",
"Created_Date":"30-06-2018",
"Received_profile":205,
"Interview_completed":100,
"Yet_to_schedule":105 
},
{
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
	a["Attachment"] = "C:/RMS/JD/" + str(a["Attachment"])
	op = randint(1005,1100)
	return jsonify(data = op)

# View Profile
b = [{
"Jd_Id":"1005",
"jd_Name":"Apple Data Engineer",
"created_date":"01-08-2018",
"Profiles": [{"email":"harmanjeetsingh121@gmail.com",
	"Exp":2,
	"Int_Stage": "Selected", 
	"Name": "Harmanjeet", 		
	"Phone_No": 9540886855, 
	"Prof_ID": 135, 
	"Profile": "www.google.com",
	"Profile_score": "82%"
  		},
		{
	"email":"raunak190r200@gmail.com",
	"Exp":2.1,
	"Int_Stage": "Selected", 
	"Name": "Kunal Raunak", 			
	"Phone_No": 9494821792, 
	"Prof_ID": 136, 
	"Profile": "www.google.com",
	"Profile_score": "76%"
  		},
		{
	"email":"ssanyal.iitr@gmail.com",
	"Exp":4.1,
	"Int_Stage": "Selected", 
	"Name": "Siddhrtha Sanyal", 		 	
	"Phone_No": 9741155528, 
	"Prof_ID": 137, 
	"Profile": "www.google.com",
	"Profile_score": "79%"
  		},
		{
	"email":"kishorekumar522@gmail.com",
	"Exp":6,
	"Int_Stage": "Selected", 
	"Name": "Kishore Yakkala", 		 	
	"Phone_No": 7204410899, 
	"Prof_ID": 138, 
	"Profile": "www.google.com",
	"Profile_score": "86%"
  		},
		{
	"email":"lp.dataninja@gmail.com",
	"Exp":7,
	"Int_Stage": "Selected", 
	"Name": "Ladle Patel", 		 	
	"Phone_No": 9742123444, 
	"Prof_ID": 139, 
	"Profile": "www.google.com",
	"Profile_score": "83%"
  		},
		{
	"email":"vndraj.k@gmail.com",
	"Exp":10,
	"Int_Stage": "Selected", 
	"Name": "KVND Rajasekar", 		 	
	"Phone_No": 9160062299, 
	"Prof_ID": 140, 
	"Profile": "www.google.com",
	"Profile_score": "72%"
  		},
		{
	"email":"arvind.anugula@gmail.com",
	"Exp":10,
	"Int_Stage": "Selected", 
	"Name": "Aravind Kumar Anugula", 		 	
	"Phone_No": 8197627896, 
	"Prof_ID": 141, 
	"Profile": "www.google.com",
	"Profile_score": "78%"
  		}]
}, {
"Jd_Id":"1001",
"jd_Name":".Net",
"created_date":"12-02-2018",
"Profiles": [{"email":"sakya@gmail.com",
	"Exp":8,
	"Int_Stage": "L0", 
	"Name": "Sakya Maiti", 		
	"Phone_No": 1234567890, 
	"Prof_ID": 123, 
	"Profile": "www.google.com",
	"Profile_score": "82%"
  		},
		{
	"email":"varun@gmail.com",
	"Exp":8,
	"Int_Stage": "Rejected", 
	"Name": "Varun Anant", 			
	"Phone_No": 1234567890, 
	"Prof_ID": 124, 
	"Profile": "www.google.com",
	"Profile_score": "52%"
  		},
		{
	"email":"abi@gmail.com",
	"Exp":8,
	"Int_Stage": "Completed", 
	"Name": "Abhi Chu", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 125, 
	"Profile": "www.google.com",
	"Profile_score": "86%"
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
	"Profile": "www.google.com",
	"Profile_score": "72%"
  		},
		{
	"email":"shalaj@gmail.com",
	"Exp":8,
	"Int_Stage": "Rejected", 
	"Name": "Shalaj", 			
	"Phone_No": 1234567890, 
	"Prof_ID": 127, 
	"Profile": "www.google.com",
	"Profile_score": "42%"
  		},
		{
	"email":"karan@gmail.com",
	"Exp":8,
	"Int_Stage": "Completed", 
	"Name": "Karan", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 128, 
	"Profile": "www.google.com",
	"Profile_score": "90%"
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
	"Profile": "www.google.com",
	"Profile_score": "52%"
  		},
		{
	"email":"babu@gmail.com",
	"Exp":8,
	"Int_Stage": "Rejected", 
	"Name": "Babu", 			
	"Phone_No": 1234567890, 
	"Prof_ID": 130, 
	"Profile": "www.google.com",
	"Profile_score": "82%"
  		},
		{
	"email":"vinod@gmail.com",
	"Exp":8,
	"Int_Stage": "Completed", 
	"Name": "Vinod", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 131, 
	"Profile": "www.google.com",
	"Profile_score": "72%"
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
	"Profile": "www.google.com",
	"Profile_score": "52%"
  		},
		{
	"email":"rakesh@gmail.com",
	"Exp":8,
	"Int_Stage": "Rejected", 
	"Name": "Rakesh", 			
	"Phone_No": 1234567890, 
	"Prof_ID": 133, 
	"Profile": "www.google.com",
	"Profile_score": "62%"
  		},
		{
	"email":"subhajit@gmail.com",
	"Exp":8,
	"Int_Stage": "Completed", 
	"Name": "Subhajit", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 134, 
	"Profile": "www.google.com",
	"Profile_score": "82%"
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

feedback= [{"Jd_Id":"1001",
"Prof_Id": "123",
"email":"sakya@gmail.com",
"Exp":8,
"Name": "Sakya Maiti", 		
"Phone_No": 1234567890,
"jd_Name":".Net",
"Prof_Staus":"Selected",
"L0_Feedback":"Good",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Good",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1001",
"Prof_Id": "124",
"email":"varun@gmail.com",
"Exp":8,
"Name": "Varun Anant", 		
"Phone_No": 1234567890,
"jd_Name":".Net",
"Prof_Staus":"Rejected",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1001",
"Prof_Id": "125",
"email":"abhi@gmail.com",
"Exp":8,
"Name": "Abhishek Ganapati", 		
"Phone_No": 1234567890,
"jd_Name":".Net",
"Prof_Staus":"Completed",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1002",
"Prof_Id": "126",
"email":"nishant@gmail.com",
"Exp":8,
"Name": "Nishant", 		
"Phone_No": 1234567890,
"jd_Name":"C#",
"Prof_Staus":"Rejected",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1002",
"Prof_Id": "127",
"email":"shalaj@gmail.com",
"Exp":8,
"Name": "Shalaj", 		
"Phone_No": 1234567890,
"jd_Name":"C#",
"Prof_Staus":"Rejected",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1002",
"Prof_Id": "128",
"email":"karan@gmail.com",
"Exp":8,
"Name": "Karan", 		
"Phone_No": 1234567890,
"jd_Name":"C#",
"Prof_Staus":"Rejected",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1003",
"Prof_Id": "129",
"email":"piyush@gmail.com",
"Exp":8,
"Name": "Piyush", 		
"Phone_No": 1234567890,
"jd_Name":"Big Data",
"Prof_Staus":"Rejected",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1003",
"Prof_Id": "130",
"email":"babu@gmail.com",
"Exp":8,
"Name": "Babu", 		
"Phone_No": 1234567890,
"jd_Name":"Big Data",
"Prof_Staus":"Rejected",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1003",
"Prof_Id": "131",
"email":"vinod@gmail.com",
"Exp":8,
"Name": "Vinod", 		
"Phone_No": 1234567890,
"jd_Name":"Big Data",
"Prof_Staus":"Rejected",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1004",
"Prof_Id": "132",
"email":"ranjan@gmail.com",
"Exp":8,
"Name": "ranjan", 		
"Phone_No": 1234567890,
"jd_Name":"UI Developer",
"Prof_Staus":"Rejected",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1004",
"Prof_Id": "133",
"email":"rakesh@gmail.com",
"Exp":8,
"Name": "Rakesh", 		
"Phone_No": 1234567890,
"jd_Name":"UI Developer",
"Prof_Staus":"Rejected",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1004",
"Prof_Id": "134",
"email":"subhajit@gmail.com",
"Exp":8,
"Name": "Subhajit", 		
"Phone_No": 1234567890,
"jd_Name":"UI Developer",
"Prof_Staus":"Rejected",
"L0_Feedback":"Poor",
"L0_Rating": "7",
"Skill_Score":{"Java":"6",".Net":"4"},
"L1_Feedback":"Poor",
"L1_Overall_Rating":"8"
},
{"Jd_Id":"1005",
"Prof_Id": "135",
"email":"harmanjeetsingh121@gmail.com",
"Exp":2,
"Name": "Harmanjeet",                                
"Phone_No": 9540886855,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"",
"L0_Rating": "7",
"Skill_Score":{"Scala": "6","No SQL / SQL DB": "7","Hadoop (Oozie, Spark and Hive)": "6" , "Storage / Retrieval": "6", "Problem Solving":"8","Communication":"8"},
"L1_Feedback":"Breadth of knowledge in all the technologies with strong Fundamentals of algorithms and data structures",
"L1_Overall_Rating":"6",
"L2_Feeback":"Strong fundamentals and logical skills and fit for role",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"1005",
"Prof_Id": "136",
"email":"raunak190r200@gmail.com",
"Exp":2.1,
"Name": "Kunal Raunak",                             
"Phone_No": 9494821792,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Good candidate",
"L0_Rating": "7",
"Skill_Score":{"Scala": "8","No SQL / SQL DB": "8","Hadoop (Oozie, Spark and Hive)": "8" , "Storage / Retrieval": "8", "Problem Solving":"7","Communication":"7"},
"L1_Feedback":"Good technical knowledge with decent problem solving and communication skills",
"L1_Overall_Rating":"8",
"L2_Feeback":"Good hand-on knowledge with hands-on exposure to the big data stack. Also, has decent communication and problem solving skills",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"1005",
"Prof_Id": "137",
"email":"ssanyal.iitr@gmail.com",
"Exp":4,
"Name": "Siddhrtha Sanyal",                      
"Phone_No": 9741155528,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very good at aptitute and puzzle solving.",
"L0_Rating": "8",
"Skill_Score":{"Scala": "6","No SQL / SQL DB": "7","Hadoop (Oozie, Spark and Hive)": "6" , "Storage / Retrieval": "6", "Problem Solving":"8","Communication":"8"},
"L1_Feedback":"Very good at coding. He have also worked on streaming data which is an added bonus.",
"L1_Overall_Rating":"9",
"L2_Feeback":"Project Experience: Two big projects. One with major beverages company and another with a telecom company. Problem Solving : Able to answer all three questions in a short span of time. Thought process was good. Algorithmic Question : Was able to Synthesize problem into smaller components and solve . Asked about de-dupe algorithms. Big Data Architecture : Understands different components of Batch and streaming data processing but lacks in depth assessment",
"L2_Overall_Rating": "8"
},
{"Jd_Id":"1005",
"Prof_Id": "138",
"email":"kishorekumar522@gmail.com",
"Exp":6,
"Name": "Kishore Yakkala",                         
"Phone_No": 7204410899,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Good coding skill on scala and hadoop",
"L0_Rating": "7",
"Skill_Score":{"Scala": "8","No SQL / SQL DB": "6","Hadoop (Oozie, Spark and Hive)": "7" , "Storage / Retrieval": "6", "Problem Solving":"8", "Communication":"7"},
"L1_Feedback":"Strong logical thinker with technical competence in the necessary areas.",
"L1_Overall_Rating":"7",
"L2_Feeback":"Good problem solver with ability to breakdown complex problems into technical tasks and solving them. Demonstrated strong understanding of Big Data",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"1005",
"Prof_Id": "139",
"email":"lp.dataninja@gmail.com",
"Exp":7,
"Name": "Ladle patel",                  
"Phone_No": 9742123444,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Has used the available libraries and common features but lacks in depth knowledge of how the language works and its idioms. Carries over some misleading knowledge from his work with Java.",
"L0_Rating": "7",
"Skill_Score":{"Scala": "6","No SQL / SQL DB": "7","Hadoop (Oozie, Spark and Hive)": "6" , "Storage / Retrieval": "8", "Problem Solving":"8","Communication":"8"},
"L1_Feedback":"Strong programming and aptitude and good with Hadoop ecosystem",
"L1_Overall_Rating":"8",
"L2_Feeback":"Strong programming skills with add on skills of AI and Machine learning",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"1005",
"Prof_Id": "140",
"email":"vndraj.k@gmail.com",
"Exp":10,
"Name": "KVND Rajasekar",                       
"Phone_No": 9160062299,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very good at aptitute and puzzle solving.",
"L0_Rating": "9",
"Skill_Score":{"Scala": "7","No SQL / SQL DB": "8","Hadoop (Oozie, Spark and Hive)": "7" , "Storage / Retrieval": "8", "Problem Solving":"9","Communication":"9"},
"L1_Feedback":"Good coding skill on python, Hadoop Map Reduce and also on data transformation part.",
"L1_Overall_Rating":"8",
"L2_Feeback":"Project Experience: Experience in Big data projects in the areas of Data Ingestion,Transformation & Data Processing (with Spark/Scala combination; averse to Map-Reduce or biased). Problem solving: Candidate was given 3 problems and was not able to answer 2 question. Thought process was on the average side. Algorithmic Question : Has done only a moderate level complexity (fuzzy logic, string matching & address merging). Scenario and Architecture: Candidate was able to call out the components clearly for 3 scenarios with in-depth analysis and justification",
"L2_Overall_Rating": "8"
},
{"Jd_Id":"1005",
"Prof_Id": "141",
"email":"arvind.anugula@gmail.com",
"Exp":10,
"Name": "Aravind Kumar Anugula",                        
"Phone_No": 8197627896,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Moderate puzzel solving skills.",
"L0_Rating": "6",
"Skill_Score":{"Scala": "8","No SQL / SQL DB": "7","Hadoop (Oozie, Spark and Hive)": "9" , "Storage / Retrieval": "6", "Problem Solving":"8","Communication":"8"},
"L1_Feedback":"Very good understanding on coding and analytical thought process",
"L1_Overall_Rating":"8",
"L2_Feeback":"Project Experience: Has good hands-on experience in Big Data Project. Has been involved in 4 Projects.Problem Solving: Was able to solve 2/3 problems in a reasonable time. Has good aptitude in Mathematics. Algorithmic Question : Has done only a moderate level complexity. Big Data Architecture : Good conceptual knowledge of Big Data but not an architect material",
"L2_Overall_Rating": "7"
}]

# View Interview Feedback
@app.route('/viewfeedback', methods=['GET'])
def viewfeedback():
	some =[]
	a = eval(request.args['questions'])
	Jd_Id = a["jdid"]
	Prof_Id = a["profid"]
	#b = eval(request.args['profid'])
	for i in range(0,len(feedback)):
		if (feedback[i]["Jd_Id"] == str(Jd_Id) and feedback[i]["Prof_Id"]== str(Prof_Id)):
			some.append(feedback[i])
		
	return jsonify(data = some)
    
	
# Add new Profile
@app.route('/newprof', methods=['GET'])
def newprof():
	a = eval(request.args['questions'])
	JD_ID = a["JD_ID"]
	First_Name = a['First_Name']
	Last_Name = a['Last_Name']
	Email  = a['Email']
	Phone_No = a['Phone_No']
	a["Attachment"] = "C:/RMS/Prof/" + str(a["Attachment"])
	op = randint(1005,1100)
	return jsonify(data = a)
	
if __name__ == '__main__':
	import logging
	logging.basicConfig(filename='error.log',level=logging.DEBUG)
	port = int(os.getenv('PORT', 5000))
	print("Starting app on port %d" % port)
	app.run(debug=True, port=port, host='0.0.0.0')
