"""
Resource: Brevets

Credit: I Copied and modified the ToDoListResource from ToDoListRESTful
"""
from flask import Response, request
from flask_restful import Resource

# You need to implement this in database/models.py
from database.models import Brevet

class Brevets(Resource):
    def get(self):
        json_object = Brevet.objects().to_json()
        return Response(json_object, mimetype="application/json", status=200)

    def post(self):
        # Read the entire request body as a JSON
        # This will fail if the request body is NOT a JSON.
        input_json = request.json

        ## Because input_json is a dictionary, we can do this:
        brevet = input_json["length"] # float
        start = input_json["start_time"] # string
        checkpoints = input_json["checkpoints"] # list
    
        # Now we can save the Brevet 
        result = Brevet(length=brevet, start_time=start, checkpoints=checkpoints).save()
        return {'_id': str(result.id)}, 200

