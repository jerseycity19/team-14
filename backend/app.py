# initial imports
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify
from flask_cors import CORS

import pymongo
from bson.objectid import ObjectId

# app and database
app = Flask(__name__)
#CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, headers='Content-Type')
app.config['TEMPLATES_AUTO_RELOAD'] = True

DB_NAME = 'shatterprooflive'
DB_HOST = ''
DB_PORT = 49365
DB_USER = 'shatterprooflive_main'
DB_PASS = 'CODEFORGOOD2019'

# connection = pymongo.mongo_client.MongoClient(DB_HOST, DB_PORT)
# db = connection[DB_NAME]
# db.authenticate(DB_USER, DB_PASS)

client = pymongo.MongoClient("mongodb+srv://shatterprooflive_main:<password>@cluster0-mcyvu.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

#------------------------------------------------------------------------------

# routes
@app.route("/")
def main():
	return render_template('index.html')


@app.route("/examplePost", methods=['POST'])
def examplePost():
	print(request.values.get("test"))
	return "test"


#------------------------------------------------------------------------------


if __name__ == "__main__":
	app.run()