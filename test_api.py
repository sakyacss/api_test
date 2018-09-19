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
		b = str(request.args['questions'])
		print("success" + b)
		return "success" + " " + b
	else:
		return "false"
app.run()
