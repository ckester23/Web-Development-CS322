"""
Resource: Brevets
"""
from flask import Response, request
from flask_restful import Resource
from datetime import datetime

# You need to implement this in database/models.py
from database.models import Brevet
from database.models import Checkpoint

class Brevets(Resource):
    def get(self):
        json_object = Brevet.objects().to_json()
        return Response(json_object, mimetype="application/json", status=200)

    def post(self):
        # Read the entire request body as a JSON
        # This will fail if the request body is NOT a JSON.
        input_json = request.json

        ## Because input_json is a dictionary, we can do this:
        brevet = input_json["length"] # Should be a string
        start = input_json["start_time"] # Should be a list of dictionaries
        # start = datetime.strptime(start, '%Y-%m-%dT%H:%M')
        checkpoints = input_json["checkpoints"]
        
        check_objects = []
        for checkpoint in checkpoints:
            km = checkpoint["km"]
            mi = checkpoint["miles"]
            loc = checkpoint["location"]
            star = checkpoint["open"]
            # star = datetime.strptime(star, '%Y-%m-%dT%H:%M')
            clos = checkpoint["close"]
            # clos = datetime.strptime(clos, '%Y-%m-%dT%H:%M')
            new_check_item = Checkpoint(km=km, miles=mi, location=loc, open=star, close=clos)
            check_objects.append(new_check_item)

        # result = Brevet(**input_json).save()
        result = Brevet(length=brevet, start_time=start, checkpoints=check_objects).save()
        return {'_id': str(result.id)}, 200


# MongoEngine queries:
# Brevet.objects() : similar to find_all. Returns a MongoEngine query
# Brevet(...).save() : creates new brevet
# Brevet.objects.get(id=...) : similar to find_one

# Two options when returning responses:
#
# return Response(json_object, mimetype="application/json", status=200)
# return python_dict, 200
#
# Why would you need both?
# Flask-RESTful's default behavior:
# Return python dictionary and status code,
# it will serialize the dictionary as a JSON.
#
# MongoEngine's objects() has a .to_json() but not a .to_dict(),
# So when you're returning a brevet / brevets, you need to convert
# it from a MongoEngine query object to a JSON and send back the JSON
# directly instead of letting Flask-RESTful attempt to convert it to a
# JSON for you.
