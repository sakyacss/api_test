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
},
{
"JD_Name": "Apple Frontend Developer",
"ID":2,
"No_of_Position":10,
"Skill_Sets":"ReactJS, AngularJS, JavaScript, HTML5",
"Created_Date":"01-11-2018",
"Received_profile":20,
"Interview_completed":15,
"Yet_to_schedule":5,
"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/jd-upload/AppleJD.docx" 
},
{
"JD_Name": "Apple Backend Developer",
"ID":3,
"No_of_Position":10,
"Skill_Sets":"Java, Spark, Hadoop",
"Created_Date":"01-11-2018",
"Received_profile":13,
"Interview_completed":12,
"Yet_to_schedule":1,
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
},
{
"Jd_Id":"2",
"jd_Name":"Apple Frontend Developer",
"created_date":"01-11-2018",
"Profiles": [{"email": "atchetna.92@gmail.com",
	"Exp":"Frontend Developer - LI Technologies Private Limited ",
	"Int_Stage": "Selected", 
	"Name": "Chetna Mahajan (Guru Gobind Singh Indrapastha University)", 		
	"Phone_No": "JavaScript, React Native Js, React Js with ESLint", 
	"Prof_ID": 156, 
	"Profile": "www.google.com",
	"Profile_Score": "80%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/ChetnaMahajan_156.pdf"
  		},
		{"email": "sikindar247@gmail.com ",
	"Exp":"Frontend Developer - Nineleaps Technologies",
	"Int_Stage": "Selected", 
	"Name": "Sikindar Mirza (Jawaharlal Nehru Technological University)", 		
	"Phone_No": "JavaScript, Ruby, C, jQuery, ReactJS, Redux ", 
	"Prof_ID": 157, 
	"Profile": "www.google.com",
	"Profile_Score": "85%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Sikindar_157.pdf"
  		},
		{"email": "jayendra.sharan@gmail.com",
	"Exp":"Senior Software Engineer - MangoApps",
	"Int_Stage": "Selected", 
	"Name": "Jayendra Sharan (National Institute of Science & Technology)", 		
	"Phone_No": "JAVASCRIPT, JQUERY, HTML, CSS, jQuery, ReactJS, Redux", 
	"Prof_ID": 158, 
	"Profile": "www.google.com",
	"Profile_Score": "87%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Jayendra_158.pdf"
  		},
		{"email": "biswaspoulima36@gmail.com",
	"Exp":"Frontend Developer - TATA CONSULTANCY SERVICES",
	"Int_Stage": "Selected", 
	"Name": "Poulima Biswas (College of Engineering & Management, Kolaghat)", 		
	"Phone_No": "HTML5, CSS3, JavaScript(ES5/ES6), React, Redux, Redux Saga, Styled components, Reselect,  AngularJS, Bootstrap, Jquery, SASS, Ionic, Cordova, Underscore js, Eslint/Jshint ", 
	"Prof_ID": 159, 
	"Profile": "www.google.com",
	"Profile_Score": "90%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Poulima_159.pdf"
  		},
		{"email": "Praveen.gupta1507@gmail.com ",
	"Exp":"Software Developer - Natural Softwares Pvt Ltd Jaipur",
	"Int_Stage": "Selected", 
	"Name": "PRAVEEN GUPTA (Rajasthan Technical University)", 		
	"Phone_No": "React JS, React Redux, Redux Thunk, HTML 5, CSS 3, Git, SQL", 
	"Prof_ID": 160, 
	"Profile": "www.google.com",
	"Profile_Score": "75%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Praveen_160.pdf"
  		},
		{"email": "rajshekarus@gmail.com ",
	"Exp":"UI Developer - Target Corporation",
	"Int_Stage": "Selected", 
	"Name": "Raja V (Osmania University)", 		
	"Phone_No": "HTML5, JavaScript, JQuery, CSS ,BootStrap, AngularJS, ReactJS", 
	"Prof_ID": 161, 
	"Profile": "www.google.com",
	"Profile_Score": "70%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Raja_161.pdf"
  		},
		{"email": "sjain2393@icloud.com ",
	"Exp":"Junior Developer - ElivoTech Solution Pvt Ltd",
	"Int_Stage": "Selected", 
	"Name": "Shubham Jain (Bharathi Vidyapeeth Deemed University)", 		
	"Phone_No": "HTML5, JavaScript, JQuery, CSS ,BootStrap, AngularJS, ReactJS", 
	"Prof_ID": 162, 
	"Profile": "www.google.com",
	"Profile_Score": "75%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Shubham_162.pdf"
  		},
		{"email": "tejaswinisankuru@gmail.com",
	"Exp":"Systems Engineer - Tata Consultancy Services ",
	"Int_Stage": "Selected", 
	"Name": "Teja Sankuru (Kakinada Institute of Engineering & Technology)", 		
	"Phone_No": " JavaScript, MySQL, HTML5, CSS3,  jQuery, Angular, React, Bootstrap, Jasmine", 
	"Prof_ID": 163, 
	"Profile": "www.google.com",
	"Profile_Score": "78%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/Teja_163.pdf"
  		}]
		},
	{
"Jd_Id":"3",
"jd_Name":"Apple Backend Developer",
"created_date":"01-11-2018",
"Profiles": [{"email": "arunkkarepu@gmail.com  ",
	"Exp":"IT Programmer Analyst - Oracle",
	"Int_Stage": "Selected", 
	"Name": "Karepu Arun Kumar (IIT Kharagpur)", 		
	"Phone_No": "Java, C#, JavaScript ", 
	"Prof_ID": 164, 
	"Profile": "www.google.com",
	"Profile_Score": "84%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/ChetnaMahajan_156.pdf"
  		},
		{"email": "kchoudhary274@gmail.com",
	"Exp":"Software Developer - Zensar Technology",
	"Int_Stage": "Selected", 
	"Name": "KRISHNA CHOUDHARY (Vellore Institute of Technology)", 		
	"Phone_No": "Java(Core), J2EE", 
	"Prof_ID": 165, 
	"Profile": "www.google.com",
	"Profile_Score": "82%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/ChetnaMahajan_156.pdf"
  		},
		{"email": "lakshmi.priyanka195@gmail.com",
	"Exp":"Senior Member Technical - ADP Private Limited",
	"Int_Stage": "Selected", 
	"Name": "Lakshmi Priyanka Dasari (GITAM University)", 		
	"Phone_No": "Springboot RESTful Web Services, RabbitMQ, MongoDB, Jenkins, GIT, Gerrit", 
	"Prof_ID": 166, 
	"Profile": "www.google.com",
	"Profile_Score": "89%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/ChetnaMahajan_156.pdf"
  		},
		{"email": "mahendersokhal@gmail.com",
	"Exp":"Senior Member Technical - Oracle India Pvt Ltd",
	"Int_Stage": "Selected", 
	"Name": "Mahender Kumar (SardarVallabhbhai National Institute of Technology)", 		
	"Phone_No": "C, C++, Java(Core Java),Data Structure And Algorithms", 
	"Prof_ID": 167, 
	"Profile": "www.google.com",
	"Profile_Score": "81%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/ChetnaMahajan_156.pdf"
  		},
		{"email": "pramodgsable@gmail.com",
	"Exp":"Software Engineer - Bhanix Finance And Investment Limited",
	"Int_Stage": "Selected", 
	"Name": "Pramod Sable (VIT University)", 		
	"Phone_No": "Java, REST webservices(JAX-RS), SOAP(JAX-WS), XML, JSON", 
	"Prof_ID": 168, 
	"Profile": "www.google.com",
	"Profile_Score": "84%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/ChetnaMahajan_156.pdf"
  		},
		{"email": "sravanamv3@gmail.com ",
	"Exp":"Senior Software Engineer - Qualcomm India",
	"Int_Stage": "Selected", 
	"Name": "Venu Madhu Kumar S (Sri Chaitanya jr.college)", 		
	"Phone_No": "Java, REST webservices(JAX-RS), SOAP(JAX-WS), XML, JSON", 
	"Prof_ID": 169, 
	"Profile": "www.google.com",
	"Profile_Score": "85%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/ChetnaMahajan_156.pdf"
  		},
		{"email": "cheekoti.vamc@gmail.com ",
	"Exp":"Senior Software Engineer - Accenture",
	"Int_Stage": "Selected", 
	"Name": "Vamshi Cheekoti (Jawaharlal Nehru Technological University)", 		
	"Phone_No": "AngularJs/Angular2/4/6*, NodeJs, JavaScript, Web Technologies, Core Java, Hibernate, Spring", 
	"Prof_ID": 170, 
	"Profile": "www.google.com",
	"Profile_Score": "85%",
	"Attachments":"https://s3.amazonaws.com/jsa-angular6-bucket6/profile/ChetnaMahajan_156.pdf"
  		}]
		}
] 
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
},
{"Jd_Id":"1",
"Prof_Id": "151",
"email":"dhiranjamana27@gmail.com",
"Exp":3,
"Name": "Dhiran Jamana",                  
"Phone_No": 9940599704,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Internal Profile",
"L0_Rating": "",
"Skill_Score":"",
"L1_Feedback":"",
"L1_Overall_Rating":"",
"L2_Feeback":"",
"L2_Overall_Rating": ""
},
{"Jd_Id":"1",
"Prof_Id": "152",
"email":"Nishanth.Nayakanti@csscorp.com",
"Exp":8,
"Name": "Nishant Nayakanti",                  
"Phone_No": 9538321077,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Internal Profile",
"L0_Rating": "",
"Skill_Score":"",
"L1_Feedback":"",
"L1_Overall_Rating":"",
"L2_Feeback":"",
"L2_Overall_Rating": ""
},
{"Jd_Id":"1",
"Prof_Id": "153",
"email":"puneet.reddy@csscorp.com",
"Exp":7,
"Name": "Puneet Reddy",                  
"Phone_No": 9160924201,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Internal Profile",
"L0_Rating": "",
"Skill_Score":"",
"L1_Feedback":"",
"L1_Overall_Rating":"",
"L2_Feeback":"",
"L2_Overall_Rating": ""
},
{"Jd_Id":"1",
"Prof_Id": "154",
"email":"shalaj.vibhore@csscorp.com",
"Exp":5,
"Name": "Shalaj Vibhore",                  
"Phone_No": 9535802882,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Internal Profile",
"L0_Rating": "",
"Skill_Score":"",
"L1_Feedback":"",
"L1_Overall_Rating":"",
"L2_Feeback":"",
"L2_Overall_Rating": ""
},
{"Jd_Id":"1",
"Prof_Id": "155",
"email":"sakya.maiti@csscorp.com",
"Exp":4,
"Name": "Sakya Maiti",                  
"Phone_No": 9980696893,
"jd_Name":"Apple Data Engineer",
"Prof_Staus":"Selected",
"L0_Feedback":"Internal Profile",
"L0_Rating": "",
"Skill_Score":"",
"L1_Feedback":"",
"L1_Overall_Rating":"",
"L2_Feeback":"",
"L2_Overall_Rating": ""
},
{"Jd_Id":"2",
"Prof_Id": "154",
"email":"atchetna.92@gmail.com",
"Exp":2.10,
"Name": "Chetna Mahajan",                                
"Phone_No": 9910327641,
"jd_Name":"Apple Frontend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"5"},{"Skill":"Leadership and Interpersonal skills ", "Score":"1"},{"Skill":"Technical competence", "Score":"5"} , {"Skill":"Subject matter knowledge", "Score":"5"}],
"L1_Feedback":"She is  having good experience on ReactJS development. She worked on few components as per her project requirements. She is having  capability to learn/work on any new ReactJS components.",
"L1_Overall_Rating":"4",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "5"
},
{"Jd_Id":"2",
"Prof_Id": "157",
"email":"sikindar247@gmail.com",
"Exp":3.6,
"Name": "Sikindar Mirza",                                
"Phone_No": 9550655247,
"jd_Name":"Apple Frontend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"6"},{"Skill":"Leadership and Interpersonal skills ", "Score":"3"},{"Skill":"Technical competence", "Score":"6"} , {"Skill":"Subject matter knowledge", "Score":"6"}],
"L1_Feedback":"He is having good capability to handle/develop ReactJS components. He is having good learning capability.",
"L1_Overall_Rating":"5",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "6"
},
{"Jd_Id":"2",
"Prof_Id": "158",
"email":"jayendra.sharan@gmail.com",
"Exp":6,
"Name": "Jayendra Sharan",                                
"Phone_No":  8007861514,
"jd_Name":"Apple Frontend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"6"},{"Skill":"Leadership and Interpersonal skills ", "Score":"3"},{"Skill":"Technical competence", "Score":"7"} , {"Skill":"Subject matter knowledge", "Score":"7"}],
"L1_Feedback":"He is good at ReactJS development. He answered most of the questions. He is  having good programming skills",
"L1_Overall_Rating":"6",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"2",
"Prof_Id": "159",
"email":"biswaspoulima36@gmail.com",
"Exp":4,
"Name": "Poulima Biswas",                                
"Phone_No":  8939326005,
"jd_Name":"Apple Frontend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"6"},{"Skill":"Leadership and Interpersonal skills ", "Score":"7"},{"Skill":"Technical competence", "Score":"7"} , {"Skill":"Subject matter knowledge", "Score":"7"}],
"L1_Feedback":"She is good in technologies .",
"L1_Overall_Rating":"7",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"2",
"Prof_Id": "160",
"email":"Praveen.gupta1507@gmail.com",
"Exp":1.8,
"Name": "PRAVEEN GUPTA",                                
"Phone_No":  7414009995,
"jd_Name":"Apple Frontend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"6"},{"Skill":"Leadership and Interpersonal skills ", "Score":"3"},{"Skill":"Technical competence", "Score":"6"} , {"Skill":"Subject matter knowledge", "Score":"6"}],
"L1_Feedback":"He just have 1.8 Years experience in software development. But he is  good at ReactJS development. He answered most of the questions. He is  having excellent capability to learn new technologies .",
"L1_Overall_Rating":"6",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"2",
"Prof_Id": "161",
"email":"rajshekarus@gmail.com",
"Exp":4,
"Name": "Raja V",                                
"Phone_No":  9000405351,
"jd_Name":"Apple Frontend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"7"},{"Skill":"Leadership and Interpersonal skills ", "Score":"7"},{"Skill":"Technical competence", "Score":"7"} , {"Skill":"Subject matter knowledge", "Score":"7"}],
"L1_Feedback":"good in technologies React JS,nodejs and Html.",
"L1_Overall_Rating":"7",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"2",
"Prof_Id": "162",
"email":"sjain2393@icloud.com",
"Exp":1.5,
"Name": "Shubham Jain",                                
"Phone_No":  7073392579,
"jd_Name":"Apple Frontend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"7"},{"Skill":"Leadership and Interpersonal skills ", "Score":"2"},{"Skill":"Technical competence", "Score":"7"} , {"Skill":"Subject matter knowledge", "Score":"6"}],
"L1_Feedback":"He is  having good programming skills. He is less experienced in IT field and having good experience in React JS development. He answered most of the questions.He is  having excellent capability to learn new technologies ",
"L1_Overall_Rating":"5",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"2",
"Prof_Id": "163",
"email":"tejaswinisankuru@gmail.com",
"Exp":3.7,
"Name": "Teja Sankuru",                                
"Phone_No": 9177278168 ,
"jd_Name":"Apple Frontend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"8"},{"Skill":"Leadership and Interpersonal skills ", "Score":"7"},{"Skill":"Technical competence", "Score":"7"} , {"Skill":"Subject matter knowledge", "Score":"7"}],
"L1_Feedback":"She is good in React JS, node JS and HTML. She have good communication skills",
"L1_Overall_Rating":"7",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"3",
"Prof_Id": "164",
"email":"arunkkarepu@gmail.com",
"Exp":3.6,
"Name": "Karepu Arun Kumar",                                
"Phone_No": 7980284185 ,
"jd_Name":"Apple Backend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"6"},{"Skill":"Leadership and Interpersonal skills ", "Score":"5"},{"Skill":"Technical competence", "Score":"5"} , {"Skill":"Subject matter knowledge", "Score":"5"}],
"L1_Feedback":"Arun  has  working experience  in multiple  technologies,  found to be a quick learner. Evaluated  as per  his strength in java , found  average  level of  technical skills   considering  4yrs of experience . He has average level  of java skills  but  has good analytical skills  and understanding of concepts.",
"L1_Overall_Rating":"6",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"3",
"Prof_Id": "165",
"email":"kchoudhary274@gmail.com",
"Exp":4.5,
"Name": "KRISHNA CHOUDHARY",                                
"Phone_No": 9674635307 ,
"jd_Name":"Apple Backend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"8"},{"Skill":"Leadership and Interpersonal skills ", "Score":"8"},{"Skill":"Technical competence", "Score":"8"} , {"Skill":"Subject matter knowledge", "Score":"8"}],
"L1_Feedback":"He is technically sound in Java/J2EE technologies.Willingness to learn new learn technologies.Have hands on experience in Java.",
"L1_Overall_Rating":"8",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"3",
"Prof_Id": "166",
"email":"lakshmi.priyanka195@gmail.com ",
"Exp":4.2,
"Name": "Lakshmi Priyanka Dasari",                                
"Phone_No": 9160866565 ,
"jd_Name":"Apple Backend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"8"},{"Skill":"Leadership and Interpersonal skills ", "Score":"8"},{"Skill":"Technical competence", "Score":"8"} , {"Skill":"Subject matter knowledge", "Score":"8"}],
"L1_Feedback":"She is good in Core Java,Spring and Hibernate.Has hands on experience in Spring MVC.Need to brush in Webservices",
"L1_Overall_Rating":"8",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"3",
"Prof_Id": "167",
"email":"mahendersokhal@gmail.com",
"Exp":5.8,
"Name": "Mahender Kumar",                                
"Phone_No": 9703206553 ,
"jd_Name":"Apple Backend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"8"},{"Skill":"Leadership and Interpersonal skills ", "Score":"8"},{"Skill":"Technical competence", "Score":"8"} , {"Skill":"Subject matter knowledge", "Score":"8"}],
"L1_Feedback":"He is good in Core Java.Don't have knowledge in Spring and back end scripting .But willing to learn new technologies",
"L1_Overall_Rating":"8",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"3",
"Prof_Id": "168",
"email":"pramodgsable@gmail.com",
"Exp":4.7,
"Name": "Pramod Sable",                                
"Phone_No": 9042122646 ,
"jd_Name":"Apple Backend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"8"},{"Skill":"Leadership and Interpersonal skills ", "Score":"8"},{"Skill":"Technical competence", "Score":"8"} , {"Skill":"Subject matter knowledge", "Score":"8"}],
"L1_Feedback":"He is good in Core Java and Spring.Has worked on Back end technologies.Willing to learn new technologies",
"L1_Overall_Rating":"8",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"3",
"Prof_Id": "169",
"email":"sravanamv3@gmail.com",
"Exp":3.8,
"Name": "Venu Madhu Kumar S",                                
"Phone_No": 7569052471 ,
"jd_Name":"Apple Backend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"8"},{"Skill":"Leadership and Interpersonal skills ", "Score":"8"},{"Skill":"Technical competence", "Score":"8"} , {"Skill":"Subject matter knowledge", "Score":"8"}],
"L1_Feedback":"Good in Core Java and Spring.He needs to scale up on the new technologies and has worked on the back end",
"L1_Overall_Rating":"8",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "7"
},
{"Jd_Id":"3",
"Prof_Id": "170",
"email":"cheekoti.vamc@gmail.com",
"Exp":8,
"Name": "Vamshi Cheekoti",                                
"Phone_No": 9491563114 ,
"jd_Name":"Apple Backend Developer",
"Prof_Staus":"Selected",
"L0_Feedback":"Very Good Coding Skill",
"L0_Rating": "7",
"Skill_Score":[{"Skill":"Communication clarity","Score":"6"},{"Skill":"Leadership and Interpersonal skills ", "Score":"5"},{"Skill":"Technical competence", "Score":"6"} , {"Skill":"Subject matter knowledge", "Score":"6"}],
"L1_Feedback":"Vamshi is having 8 years of experience having  good technical skills on Angular JS , HTML 5  and UI related  technologies . He has basic knowledge on the core and sql Plsql areas . He has good analytical skills and a quick learner",
"L1_Overall_Rating":"6",
"L2_Feeback":"Fit for the role. Good hands-on experience",
"L2_Overall_Rating": "6"
}
]

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
	Last_Comp_Name = a['Last_Comp_Name']
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
