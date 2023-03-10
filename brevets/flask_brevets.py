"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""
import os
import logging
import flask
import requests
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import json

###
# Globals
###
app = flask.Flask(__name__)
app.debug = True if "DEBUG" not in os.environ else os.environ["DEBUG"]
port_num = True if "PORT" not in os.environ else os.environ["PORT"]
app.logger.setLevel(logging.DEBUG)


### API Callers ###

API_ADDR = os.environ["API_ADDR"]
API_PORT = os.environ["API_PORT"]
API_URL = f"http://{API_ADDR}:{API_PORT}/api/"

def brevet_insert(brevet_dist, start_time, checkpoints):
    """
    Inserts a new table into the database by calling the API.
    Inputs a brevet (string), a start time (string), and checkpoints (list of dictionaries)

    Returns the unique ID assigned to the document by mongo (primary key)

    This is copied from ToDoListRESTful and modified 
    """
    _id = requests.post(f"{API_URL}/brevets", json={"length": brevet_dist, "start_time": start_time, "checkpoints": checkpoints}).json()
    return _id

def brevet_find():
    """
    Obtains the newest document in the "tables" collection in database by calling the API.

    Returns brevet (string), start time(string), and checkpoints (list of dictionaries)
    as a tuple.

    This is copied from ToDoListRESTful and modified 
    """
    brevets = requests.get(f"{API_URL}/brevets").json()

    brevet = brevets[-1]
    return brevet["length"], brevet["start_time"], brevet["checkpoints"]  

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############

# need two more app.route(); one for find, one for insert
# get info same as getting km

@app.route("/insert_brevet", methods=["POST"])
def insert_brevet():
    """
    /insert_brevet : Inserts the current table into the database
    Returns an error message if the table is empty

    Only accepts POST requests

    JSON interface: gets JSON, responds with JSON
    """
    app.logger.debug("Got a JSON request: INSERT")
    try:
        # Read the entire request body as a JSON
        # This will fail if the request body is NOT a JSON.
        input_json = request.json
        app.logger.debug(input_json)
        # if successful, input_json is automatically parsed into a python dictionary!
        
        # Because input_json is a dictionary, we can do this:
        brevet = input_json["length"] # Should be a string
        start = input_json["start_time"] # Should be a formatted string
        checkpoints = input_json["checkpoints"]  # Should be a list of dicts

        # If the user didn't input any checkpoints, return an error message
        if (checkpoints == []):
            return flask.jsonify(result={},
                        message="Oh no! Input Error", 
                        status=0, 
                        mongo_id='None')
        
        # Other wise, call the insert function in mypymongo.py
        table_id = brevet_insert(brevet, start, checkpoints)

        return flask.jsonify(result={},
                        message="Inserted!", 
                        status=1, # This is defined by you. You just read this value in your javascript.
                        mongo_id=table_id)
    except:
        # The reason for the try and except is to ensure Flask responds with a JSON.
        # If Flask catches your error, it means you didn't catch it yourself,
        # And Flask, by default, returns the error in an HTML.
        # We want /insert to respond with a JSON no matter what!
        return flask.jsonify(result={},
                        message="Oh no! Server error!", 
                        status=0, 
                        mongo_id='None')

@app.route("/fetch_brevet")
def fetch_brevet():
    """
    /fetch_brevet : fetches the newest table from the database.

    Accepts GET requests ONLY!

    JSON interface: gets JSON, responds with JSON
    """
    app.logger.debug("Got a JSON request: FETCH")

    try:
        # don't have to worry about errors here, so we can call 
        # the function in mypymongo.py
        brevet, start, checkpoints = brevet_find()
        return flask.jsonify(
                result={"length": brevet, "start_time": start, "checkpoints": checkpoints}, 
                status=1,
                message="Successfully fetched a table!")
    except:
        return flask.jsonify(
                result={}, 
                status=0,
                message="Something went wrong, couldn't fetch any tables!")


@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")

    # Get our values from HTML
    km = request.args.get('km', 999, type=float) # default value 999
    brevet_dist = request.args.get('brevet_dist', 999, type=float)
    start_time = request.args.get('start_time', "2023-02-1700:00", type=str) 
    start_time = arrow.get(start_time, "YYYY-MM-DDTHH:mm") 

    app.logger.debug("km={}".format(km))
    app.logger.debug("brev={}".format(brevet_dist))
    app.logger.debug("start={}".format(start_time))
    app.logger.debug("request.args: {}".format(request.args))
    
    # Now passes the User's desired start time and brevet distance
    open_time = acp_times.open_time(km, brevet_dist, start_time).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, brevet_dist, start_time).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


#############

if __name__ == "__main__":
    # may write a fail case for this if you want
    app.run(port=port_num, host="0.0.0.0")
