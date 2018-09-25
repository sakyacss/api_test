from __future__ import print_function
import flask
from flask import request, jsonify
import re, math
from flask_cors import CORS
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


@app.route('/addjd', methods=['GET'])
def addjd():
               
    a= [{
"JD Name": ".Net",
"ID":1001,
"No of Position":200,
"Skill Sets":".Net",
"Created Date":"10-8-2018",
"Received profile":100,
"Interview completed":50,
"Yet to schedule":50 
},

{
"JD Name": "C#",
"ID":1002,
"No of Position":200,
"Skill Sets":"C#",
"Created Date":"12-8-2018",
"Received profile":120,
"Interview completed":50,
"Yet to schedule":70 
},

{
"JD Name": "Big Data",
"ID":1003,
"No of Position":100,
"Skill Sets":"Hadoop,Spark,Scala",
"Created Date":"12-8-2018",
"Received profile":80,
"Interview completed":50,
"Yet to schedule":30 
},
{
"JD Name": "UI Developer",
"ID":1004,
"No of Position":50,
"Skill Sets":"Angular,Nodejs",
"Created Date":"16-8-2018",
"Received profile":40,
"Interview completed":10,
"Yet to schedule":30}
]

    
    return jsonify(data = a)
if __name__ == '__main__':
	import logging
	logging.basicConfig(filename='error.log',level=logging.DEBUG)
	port = int(os.getenv('PORT', 5000))
	print("Starting app on port %d" % port)
	app.run(debug=True, port=port, host='0.0.0.0')
