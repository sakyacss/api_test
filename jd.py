from __future__ import print_function
import flask
from flask import Flask, request, jsonify, render_template
from werkzeug import secure_filename
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

@app.route('/')
def home():
    return render_template("upload.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		
		f = request.files['file']
		f.save(secure_filename(f.filename))
		return 'file uploaded successfully'

@app.route('/authenticate', methods=['Get'])
def authenticate():
	a = eval(request.args['questions'])
	id = a["id"]
	pwd = a["pwd"]
	if (id == "apple-admin" and pwd == "Drowassp321"):
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
"ID":1,
"No_of_Position":35,
"Skill_Sets":"Scala, Spark, Hadoop, MapReduce, Python",
"Created_Date":"30-06-2018",
"Received_profile":198,
"Interview_completed":94,
"Yet_to_schedule":18,
"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/jd-upload/AppleJD.docx" 
}]


    
    return jsonify(data = a)

# ADD New JD
@app.route('/addjobdesc', methods=['GET'])
def addjobdesc( ):
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
"Jd_Id":"1",
"jd_Name":"Apple Data Engineer",
"created_date":"01-08-2018",
"Profiles": [{"email":"harmanjeetsingh121@gmail.com",
	"Exp":"Data Engineer - Times Internet",
	"Int_Stage": "Selected", 
	"Name": "Harmanjeet (Guru Gobind Singh Indrapastha University)", 		
	"Phone_No": "Spark, Hadoop, MapReduce, Sqoop, HDFS, Kafka", 
	"Prof_ID": 135, 
	"Profile": "www.google.com",
	"Profile_Score": "82%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/HarmanjeetSingh_135.pdf"
  		},
		{
	"email":"raunak190r200@gmail.com",
	"Exp":"Data Engineer - Bank Of America",
	"Int_Stage": "Selected", 
	"Name": "Kunal Raunak (IIT Hyderabad)", 			
	"Phone_No": "Scala, Spark, HDFS, MapReduce, Sqoop", 
	"Prof_ID": 136, 
	"Profile": "www.google.com",
	"Profile_Score": "76%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Kunal_Raunak_136.docx"
  		},
		{
	"email":"kishorekumar522@gmail.com",
	"Exp":"Data Engineer - Amadeus Labs",
	"Int_Stage": "Selected", 
	"Name": "Kishore Yakkala (JNTU)", 		 	
	"Phone_No": "Scala, Spark,Apache Tomcat, Oracle Weblogic servers, Cassandra", 
	"Prof_ID": 138, 
	"Profile": "www.google.com",
	"Profile_Score": "86%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Kishore_Yakkala_138.doc"
  		},
		{
	"email":"lp.dataninja@gmail.com",
	"Exp":"Data Scientist - GENPACT LABS",
	"Int_Stage": "Selected", 
	"Name": "Ladle Patel (Visvesvaraya Technological University)", 		 	
	"Phone_No": "Spark, TensorFlow, KerasSpark, Cassandra & MongoDB, Python", 
	"Prof_ID": 139, 
	"Profile": "www.google.com",
	"Profile_Score": "83%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Ladle_Patel_139.pdf"
  		},
		{
	"email":"mohit_516@yahoo.co.in",
	"Exp":"Lead Data Engineer - Times Internet",
	"Int_Stage": "Selected", 
	"Name": "Mohit Kundra (JRN Rajasthan Vidyapeeth University)", 		 	
	"Phone_No": "Hadoop, Hive, Pig, Cassandra, Spark", 
	"Prof_ID": 141, 
	"Profile": "www.google.com",
	"Profile_Score": "78%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Mohit_Kundra_141.pdf"
  		},

	
{"email":"tsharankumar19@gmail.com",
	"Exp":"Data Engineer - Virtusa",
	"Int_Stage": "Selected", 
	"Name": "T Sharan Kumar (JNTU)", 		 	
	"Phone_No": "Java, Hadoop, AWS, HDFS, Hive, Spark and MapReduce", 
	"Prof_ID": 145, 
	"Profile": "www.google.com",
	"Profile_Score": "76%",
 	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/T_Sharan+_Kumar_145.pdf"
  		},
	
	    {"email":"bheemeshr@gmail.com",
	"Exp":"Lead Data Engineer - Infosys Technologies Ltd.",
	"Int_Stage": "Selected", 
	"Name": "B Bheemeswar Reddy (Siva Sivani Institute of Management)", 		 	
	"Phone_No": "Hadoop, Hive, Spark ML, Scala, Play Framework, Kafka", 
	"Prof_ID": 148, 
	"Profile": "www.google.com",
	"Profile_Score": "76%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/BBheemeswarReddy_148.docx"
  		},
		{"email":"srilathabandari30@gmail.com",
	"Exp":"Lead Data Engineer - GGK Technologies",
	"Int_Stage": "Selected", 
	"Name": "Srilatha Bandari (JNTU)", 		 	
	"Phone_No": "Scala, Spark, Hadoop, MapReduce, Python", 
	"Prof_ID": 149, 
	"Profile": "www.google.com",
	"Profile_Score": "70%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Srilatha_Bandari_149.doc"
  		},
		{"email":"sekh09@gmail.com",
	"Exp":"Lead Data Engineer - Real Page India",
	"Int_Stage": "Selected" , 
	"Name": "Pulagam Sudha Sekhar (SRKR Engineering college)", 		 	
	"Phone_No": "Scala, Spark, Hadoop, MapReduce, Python", 
	"Prof_ID": 150, 
	"Profile": "www.google.com",
	"Profile_Score": "81%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Pulagam_Sudha_Sekhar_150.docx"
  		},
	    {"email":" dhiranjamana27@gmail.com",
	"Exp":"Data Engineer - Tech aspect solutions",
	"Int_Stage": "Selected", 
	"Name": "Dhiran Jamana (IIT Chennai)", 		 	
	"Phone_No": "Hadoop, Hive, Spark ML,TensorFlow,Python", 
	"Prof_ID": 151, 
	"Profile": "www.google.com",
	"Profile_Score": "89%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Dhiran_Jamana_151.pdf"
  		},
		{"email":"Nishanth.Nayakanti@csscorp.com",
	"Exp":"Lead Data Engineer",
	"Int_Stage": "Selected", 
	"Name": "Nishant Nayakanti (BITS, Pilani)", 		 	
	"Phone_No": "Scala, Spark, Python, Java, Javascript,Hadoop, Hive, pig, TensorFlow", 
	"Prof_ID": 152, 
	"Profile": "www.google.com",
	"Profile_Score": "87%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Nishanth_Nayakanti_152.pptx"
  		},
		{"email":"puneet.reddy@csscorp.com",
	"Exp":"Lead Data Engineer",
	"Int_Stage": "Selected" , 
	"Name": "Puneet Reddy (The University of Pennsylvania)", 		 	
	"Phone_No": "Scala, Spark, Hadoop, MapReduce, Python, Oozie, Kafka", 
	"Prof_ID": 153, 
	"Profile": "www.google.com",
	"Profile_Score": "89%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Puneet_Reddy_153.pptx"
  		},{"email":"shalaj.vibhore@csscorp.com",
	"Exp":"Data Scientist",
	"Int_Stage": "Selected", 
	"Name": "Shalaj Vibhore (Bangalore Institute of Technology)", 		 	
	"Phone_No": "Python, C++, Java,Apache Beam, Django, Hadoop, Hive, TensorFlow", 
	"Prof_ID": 154, 
	"Profile": "www.google.com",
	"Profile_Score": "87%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Shalaj_Vibhore_154.pptx"
  		},
		{"email":"sakya.maiti@csscorp.com",
	"Exp":"Data Scientist",
	"Int_Stage": "Selected" , 
	"Name": "Sakya Maiti (Haldia Institute of Technology)", 		 	
	"Phone_No": "Python, R ,  Flask, Dialogflow, Apache Beam, Hadoop", 
	"Prof_ID": 155, 
	"Profile": "www.google.com",
	"Profile_Score": "72%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Sakya_Maiti_155.pptx"
  		}
	    ]
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

feedback= [
{"Jd_Id":"1",
"Prof_Id": "135",
"email":"harmanjeetsingh121@gmail.com",
"Exp":2,
"Name": "Harmanjeet",                                
"Phone_No": "9540886855",
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Scala","Score":"6"},{"Skill":"No SQL / SQL DB", "Score":"7"},{"Skill":"Hadoop (Oozie, Spark and Hive)", "Score":"6"} , {"Skill":"Storage / Retrieval", "Score":"6"}, {"Skill":"Problem Solving", "Score":"8"}, {"Skill":"Communication","Score":"8"}],
"L1_Feedback":"Breadth of knowledge in all the technologies with strong Fundamentals of algorithms and data structures",
"L1_Overall_Rating":"6",
"L2_Feeback":"Strong fundamentals and logical skills and fit for role",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"1",
"Prof_Id": "136",
"email":"raunak190r200@gmail.com",
"Exp":2.1,
"Name": "Kunal Raunak",                             
"Phone_No": 9494821792,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Good candidate",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Scala","Score":"8"},{"Skill":"No SQL / SQL DB", "Score":"7"},{"Skill":"Hadoop (Oozie, Spark and Hive)", "Score":"8"} , {"Skill":"Storage / Retrieval", "Score":"7"}, {"Skill":"Problem Solving", "Score":"8"}, {"Skill":"Communication","Score":"8"}],
"L1_Feedback":"Good experience in Scala, Spark, Oozie and NOSQL database. He has basic knowledge of Web services and HTML/JSP. Selected for next round",
"L1_Overall_Rating":"8",
"L2_Feeback":"Good hands-on knowledge with hands-on exposure to the big data stack. Also, has decent communication and problem solving skills",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"1",
"Prof_Id": "138",
"email":"kishorekumar522@gmail.com",
"Exp":6,
"Name": "Kishore Yakkala",                         
"Phone_No": 7204410899,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Good coding skill on scala and hadoop",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Scala","Score":"8"},{"Skill":"No SQL / SQL DB", "Score":"6"},{"Skill":"Hadoop (Oozie, Spark and Hive)", "Score":"7"} , {"Skill":"Storage / Retrieval", "Score":"6"}, {"Skill":"Problem Solving", "Score":"8"}, {"Skill":"Communication","Score":"8"}],
"L1_Feedback":"He has good experience in scala. He has experience in Hadoop systems, he doesn't have much experience in Hive. He has experience in Rest service. He has knowledge of NoSQL databases. He understands the problem and Analysis effective. I recommend him further round ",
"L1_Overall_Rating":"7",
"L2_Feeback":"Good problem solver with ability to breakdown complex problems into technical tasks and solving them. Demonstrated strong understanding of Big Data",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"1",
"Prof_Id": "139",
"email":"lp.dataninja@gmail.com",
"Exp":7,
"Name": "Ladle patel",                  
"Phone_No": 9742123444,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Has used the available libraries and common features but lacks in depth knowledge of how the language works and its idioms. Carries over some misleading knowledge from his work with Java.",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Scala","Score":"7"},{"Skill":"No SQL / SQL DB", "Score":"7"},{"Skill":"Hadoop (Oozie, Spark and Hive)", "Score":"8"} , {"Skill":"Storage / Retrieval", "Score":"8"}, {"Skill":"Problem Solving", "Score":"8"}, {"Skill":"Communication","Score":"8"}],
"L1_Feedback":"Have good experience in coding and machine learning. Worked with Scala,Spark, Python and other related languages. Selected for next roundi",
"L1_Overall_Rating":"8",
"L2_Feeback":"Strong programming skills with add on skills of AI and Machine learning",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"1",
"Prof_Id": "141",
"email":"mohit_516@yahoo.co.in",
"Exp":11,
"Name": "Mohit Kundra",                        
"Phone_No": 8800787968,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Moderate puzzel solving skills.",
"L0_Rating": "6",
"Skill_Score":[{"Skill":"Scala","Score":"2"},{"Skill":"No SQL / SQL DB", "Score":"7"},{"Skill":"Hadoop (Oozie, Spark and Hive)", "Score":"7"} , {"Skill":"Storage / Retrieval", "Score":"6"}, {"Skill":"Problem Solving", "Score":"7"}, {"Skill":"Communication","Score":"7"}],
"L1_Feedback":"He Doesn't have much experience in scala, but his experience level of Java is good and I think he can pick up very fast. He has very  good experience in  Hive and spark. He has basic  experience in Rest service. He has good knowledge of NoSQL databases His way of analysis is alright",
"L1_Overall_Rating":"8",
"L2_Feeback":"Project Experience: Has good hands-on experience in Big Data Project. Has been involved in 4 Projects.Problem Solving: Was able to solve 2/3 problems in a reasonable time. Has good aptitude in Mathematics. Algorithmic Question : Has done only a moderate level complexity. Big Data Architecture : Good conceptual knowledge of Big Data but not an architect material",
"L2_Overall_Rating": "7"
},		
{"Jd_Id":"1",
"Prof_Id": "145",
"email":"tsharankumar19@gmail.com",
"Exp":2.4,
"Name": "T Sharan Kumar",                                
"Phone_No": 9160348626,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Scala","Score":"6"},{"Skill":"No SQL / SQL DB", "Score":"5"},{"Skill":"Hadoop (Oozie, Spark and Hive)", "Score":"7"} , {"Skill":"Storage / Retrieval", "Score":"7"}, {"Skill":"Problem Solving", "Score":"6"}, {"Skill":"Communication","Score":"7"}],
"L1_Feedback":"Good in Java Programming. Has problem solving skills. Also have good learning attitude",
"L1_Overall_Rating":"7",
"L2_Feeback":"Strong fundamentals and logical skills and fit for role",
"L2_Overall_Rating": "7"
},	
{"Jd_Id":"1",
"Prof_Id": "148",
"email":"bheemeshr@gmail.com",
"Exp":18,
"Name": "B Bheemeswar Reddy",                                
"Phone_No": 8297793903,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Scala","Score":"6.5"},{"Skill":"No SQL / SQL DB", "Score":"7"},{"Skill":"Hadoop (Oozie, Spark and Hive)", "Score":"8"} , {"Skill":"Storage / Retrieval", "Score":"7"}, {"Skill":"Problem Solving", "Score":"8"}, {"Skill":"Communication","Score":"9"}],
"L1_Feedback":"ood experience in Spark, Python, SQL and architecting. Selected for next round.",
"L1_Overall_Rating":"8",
"L2_Feeback":"Project Experience: Very good hands-on Experience. In-depth understanding of Big Data concepts. Good experience Big Data Engineering components.Problem Solving: Not Evaluated. Algorithmic Question : Good implementation knowledge in Map-Reduce & Spark in-memory processing.Big Data Architecture : Very good conceptual knowledge and application aspects.",
"L2_Overall_Rating": "8"
},
{"Jd_Id":"1",
"Prof_Id": "149",
"email":"srilathabandari30@gmail.com",
"Exp":6.3,
"Name": "Srilatha Bandari",                                
"Phone_No": 9912565288,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Scala","Score":"6"},{"Skill":"No SQL / SQL DB", "Score":"4"},{"Skill":"Hadoop (Oozie, Spark and Hive)", "Score":"6"} , {"Skill":"Storage / Retrieval", "Score":"6"}, {"Skill":"Problem Solving", "Score":"6"}, {"Skill":"Communication","Score":"6"}],
"L1_Feedback":"Good with Scala, Spark and Hadoop. She is a quick learner and logically strong.",
"L1_Overall_Rating":"7",
"L2_Feeback":"Strong fundamentals and logical skills and fit for role",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"1",
"Prof_Id": "150",
"email":"sekh09@gmail.com",
"Exp":6.1,
"Name": "Pulagam Sudha Sekhar",                                
"Phone_No": 9043047997,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Scala","Score":"5"},{"Skill":"No SQL / SQL DB", "Score":"5"},{"Skill":"Hadoop (Oozie, Spark and Hive)", "Score":"5"} , {"Skill":"Storage / Retrieval", "Score":"5"}, {"Skill":"Problem Solving", "Score":"5"}, {"Skill":"Communication","Score":"6"}],
"L1_Feedback":"Candidate is good in Hadoop, Map/Reduce(using Java), Scala, Spark. He is interested in learning new technologies",
"L1_Overall_Rating":"5",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "6"
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

# Add Feedback
@app.route('/addfeedback', methods=['GET'])
def addfeedback():
	some=[]
	a = eval(request.args['questions'])
	Jd_Id = a["jdid"]
	Prof_Id = a["profid"]
	Core_Competency = a["Core_Competency"]
	General_Competency = a['General_Competency']
	Overall_Rating = a['Overall_Rating']
	for i in range(0,len(feedback)):
		if(feedback[i]["Jd_Id"]==str(Jd_Id) and feedback[i]["Prof_Id"]==str(Prof_Id)):
			some.append(feedback[i]["Name"])
			some.append(feedback[i]["email"])
			some.append(feedback[i]["Exp"])
			some.append(feedback[i]["jd_Name"])
			for j in range(0,len(feedback[i]["Skill_Score"])):
				some.append(feedback[i]["Skill_Score"][j]["Skill"])
			op = randint(1005,1100)
			some.append(op)
	return jsonify(data = some)    
	
# Add new Profile
@app.route('/newprof', methods=['GET'])
def newprof():
	a = eval(request.args['questions'])
	JD_ID = a["JD_ID"]
	First_Name = a['First_Name']
	Middle_Name = a['Middle_Name']
	Last_Name = a['Last_Name']
	Email  = a['Email']
	University = a['University']
	Phone_No = a['Phone_No']
	Experience = a['Exp']
	Emp_Skill = a['Emp_Skill']
	Last_Comp_Name = a['Last_Comp_Name]
	a["Attachment"] = "C:/RMS/Prof/" + str(a["Attachment"])
	op = randint(1005,1100)
	return jsonify(data = op)

# Admin Page
@app.route('/admin', methods=['GET'])
def admin():
	a = eval(request.args['questions'])
	BU_Name = a["BU_Name"]
	Designation = a['Designation']
	Skill = a['Skill']
	Exp = a['Exp']
	a["Attachment"] = "C:/RMS/Prof/" + str(a["Attachment"])
	op = randint(1005,1100)
	return jsonify(data = op)

x = [{"Prof_ID":"123",
"email":"sakya@gmail.com",
"Name": "Sakya Maiti",
"JD_ID":"1",
"JD_Name":"Apple Data Engineer",
"BU_Name":"DES",
"Question_Bank":[{"q_id":"1", "Question": "What is BigQuery1111","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"bbbb","Marks":"1"},
{"q_id":"2", "Question": "What is BigQuery3333","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"cccc","Marks":"1"},
{"q_id":"3", "Question": "What is BigQuery4444","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"dddd","Marks":"1"},
{"q_id":"4", "Question": "What is BigQuery5555","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"aaaa","Marks":"1"},
{"q_id":"5", "Question": "What is BigQuery6666","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"bbbb","Marks":"1"},
{"q_id":"6", "Question": "What is BigQuery7777","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"cccc","Marks":"1"},
{"q_id":"7", "Question": "What is BigQuery8888","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"dddd","Marks":"1"},
{"q_id":"8", "Question": "What is BigQuery9999","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"bbbb","Marks":"1"},
{"q_id":"9", "Question": "What is BigQuery1010","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"aaaa","Marks":"1"},
{"q_id":"10", "Question": "What is BigQuery1112","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"cccc","Marks":"1"}]
},
{"Prof_ID":"124",
"email":"varun@gmail.com",
"Name": "Varun Anant",
"JD_ID":"1",
"JD_Name":"Apple Data Engineer",
"BU_Name":"DES",
"Question_Bank":[{"q_id":"1", "Question": "What is BigQuery2345","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"aaaa","Marks":"1"},
{"q_id":"2", "Question": "What is BigQuery2222","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"bbbb","Marks":"1"},
{"q_id":"3", "Question": "What is BigQuery3456","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"cccc","Marks":"1"},
{"q_id":"4", "Question": "What is BigQuery4567","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"dddd","Marks":"1"},
{"q_id":"5", "Question": "What is BigQuery5678","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"aaaa","Marks":"1"},
{"q_id":"6", "Question": "What is BigQuery6789","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"bbbb","Marks":"1"},
{"q_id":"7", "Question": "What is BigQuery7890","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"cccc","Marks":"1"},
{"q_id":"8", "Question": "What is BigQuery8901","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"dddd","Marks":"1"},
{"q_id":"9", "Question": "What is BigQuery9012","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"aaaa","Marks":"1"},
{"q_id":"10", "Question": "What is BigQuery0123","Option1":"aaaa","Option2":"bbbb","Option3":"cccc","Option4":"dddd","Answer":"bbbb","Marks":"1"}]
}]

@app.route('/onlinetest', methods = ['GET'])
def online_test():
	a = eval(request.args['questions'])
	Prof_ID = a["profid"]
	Email = a["email"]
	some = []
	for i in range(0,len(x)):
		if(x[i]["Prof_ID"]==str(Prof_ID) and x[i]["email"]==str(Email)):
			some.append(x[i])
	return jsonify(data = some)

@app.route('/onlinetest-result', methods = ['GET'])
def online_test_result():
	a = eval(request.args['questions'])
	Prof_ID = a["profid"]
	Score = a["score"]
	return "Score Updated"

@app.route('/executive-dashboard', methods = ['GET'])
def executive_dashboard():
	a= [{"JD_Count":"13",
	"Tot_Prof_Received" : "500",
	"Offers_Accepted": "120",
	"Offers_Rejected":"20",
	"Last_3_month_stats":[{"Month": "October","Prof_Received":"100","L0_Cleared":"90","L1_Cleared":"40","L2_Cleared":"20"},
	{"Month": "September","Prof_Received":"100","L0_Cleared":"90","L1_Cleared":"40","L2_Cleared":"20"},
	{"Month": "August","Prof_Received":"100","L0_Cleared":"90","L1_Cleared":"40","L2_Cleared":"20"}],
	"Last_3_Offered_Profiles":[{
	"email":"vinod@gmail.com",
	"Exp":8,
	"Int_Stage": "Selected", 
	"Name": "Vinod", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 131, 
	"Profile": "www.google.com",
	"Profile_Score": "72%"
  		},{
	"email":"vinod@gmail.com",
	"Exp":8,
	"Int_Stage": "Selected", 
	"Name": "Vinod", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 131, 
	"Profile": "www.google.com",
	"Profile_Score": "72%"
  		},
		{
	"email":"vinod@gmail.com",
	"Exp":8,
	"Int_Stage": "Selected", 
	"Name": "Vinod", 		 	
	"Phone_No": 1234567890, 
	"Prof_ID": 131, 
	"Profile": "www.google.com",
	"Profile_Score": "72%"
  		}]
		}]
		
	return jsonify(data = a)
	
if __name__ == '__main__':
	import logging
	logging.basicConfig(filename='error.log',level=logging.DEBUG)
	port = int(os.getenv('PORT', 5000))
	print("Starting app on port %d" % port)
	app.run(debug=True, port=port, host='0.0.0.0')
