"""
Brevets RESTful API

Credit: I Copied and modified the flask_api from ToDoListRESTful
"""
import logging
import os
from flask import Flask
from flask_restful import Api
from mongoengine import connect

# Implement two resources: Brevet and Brevets.
from resources.brevet import Brevet
from resources.brevets import Brevets

# Connect MongoEngine to mongodb
connect(host=f"mongodb://{os.environ['MONGODB_HOSTNAME']}:27017/brevetsdb")

# Start Flask app and Api here:
app = Flask(__name__)

# python lets us to if else statements on a single line
# verify that the env variables exist before setting them
app.debug = True if "DEBUG" not in os.environ else os.environ["DEBUG"]
port_num = True if "PORT" not in os.environ else os.environ["PORT"]
app.logger.setLevel(logging.DEBUG)

# instantiate the API
api = Api(app)

# Bind resources to paths here:
api.add_resource(Brevet, "/api/brevet/<id>")
api.add_resource(Brevets, "/api/brevets")

if __name__ == "__main__":
    # Run flask app normally
    app.run(port=port_num, host="0.0.0.0")
