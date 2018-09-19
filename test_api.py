from __future__ import print_function
import flask
from flask import request, jsonify
import re, math
#from collections import Counter
#from google.cloud import bigquery
#from google.oauth2 import service_account
import pandas as pd
#from pandas.io import gbq
import json
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>API</h1><p>Test Api</p>"

@app.route('/api', methods=['GET'])
def addjd():
    if 'questions' in request.args:
		#b = request.get('id')
		#c = request.get('skill')
		#df = pd.read_excel("C:/Users/css114121/Desktop/Sanofi/JD.xlsx")
		#df1= pd.DataFrame([[b,c]],columns=['JD ID','Skill name'])
		#df = df.append(df1)
		#df.to_excel("C:/Users/css114121/Desktop/Sanofi/JD.xlsx",index=False)
		b = str(request.args['questions'])
		#d = json.loads(b)
		#print(d)
		#c = str(d[0]["id"])
		#print(c)
		print("success" + b)
		return "success" + " " + b
    else:
        return "false"
app.run()
