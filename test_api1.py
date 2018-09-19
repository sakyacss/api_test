from __future__ import print_function
import flask
from flask import request, jsonify
import re, math
import pandas as pd
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
		print("success" + " " +b)
		return "success" + " " + b
	else:
		return "false"

if __name__ == '__main__':
	import logging
	logging.basicConfig(filename='error.log',level=logging.DEBUG)
	port = int(os.getenv('PORT', 5000))
	print("Starting app on port %d" % port)
	app.run(debug=True, port=port, host='0.0.0.0')
