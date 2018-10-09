#from dbconnect import connection
import flask
from flask import request, jsonify
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@bobmarley123@localhost/test_db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def home():
	try:
		#c, conn = connection()
		query = text("SELECT * from add_new_hiring1")
		data = db.engine.execute(query)
		names = []
		for row in data:
			names.append(row[0])
			names.append(row[1])
		return jsonify(data = names)
	except Exception as e:
		return (str(e))
    
if __name__ == '__main__':


    #port = int(os.getenv('PORT', 5000))
    port = int(os.environ.get("PORT", 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
