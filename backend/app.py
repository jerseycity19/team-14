# initial imports
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify
from flask_cors import CORS, cross_origin

import pymongo
from bson.objectid import ObjectId

# app and database
app = Flask(__name__)
#CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, headers='Content-Type')
app.config['TEMPLATES_AUTO_RELOAD'] = True

client = pymongo.MongoClient("mongodb+srv://shatterprooflive_main:CODEFORGOOD2019@cluster1-q2pxb.mongodb.net/")
db = client.shatterprooflive
print(db)

#------------------------------------------------------------------------------

# routes
@app.route("/")
def main():
	cursor = db.users.find({})
	patients = []
	for c in cursor:
		patients.append(c)
	return render_template('index.html', patients=patients)


@app.route("/new_user", methods=['POST'])
def new_user():
	res = request.get_json(force=True)
	query = {
		"firstname": res['first name'],
		"lastname": res['last name'],
		"propic": res['profile pic url'],
		"gender": res['gender'],
		"provider": "Dr. Srihari Sritharan"
	}

	if query.firstname is None or query.lastname is None:
		return

	cursor = db.users.find(query)
	if cursor.count() == 0:
		print("new user!")
		result = db.users.insert_one(query).inserted_id
	return ""

@app.route("/patient/<string:user_id>")
def patient(user_id):
	cursor = db.patients.find({'_id': ObjectId(user_id)})

	for key,val in scores.items():
		total = 0
		if val:
			for v in val:
				total += button_to_val[key][v]
		num_scores["depression"][key] += total
		print(key, num_scores["depression"][key])

	return render_template('patient.html', patient=cursor[0]
										 , num_scores=num_scores)

@app.route("/analytics", methods=['GET'])
def go_to_analytics():
	return render_template('analytics.html')

@app.route("/about", methods=['GET'])
def go_to_about():
	return render_template('about.html')
#------------------------------------------------------------------------------

if __name__ == "__main__":
	app.run()