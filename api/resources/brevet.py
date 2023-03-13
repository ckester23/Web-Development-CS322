"""
Resource: Brevet

Credit: I Copied and modified the ToDoListResource from ToDoListRESTful
"""
from flask import Response, request
from flask_restful import Resource

# You need to implement this in database/models.py
from database.models import Brevet

class BrevetResource(Resource):
    def get(self, id):
        brevet = Brevet.objects.get(id=id).to_json()
        return Response(brevet, mimetype="application/json", status=200)

    def put(self, id):
        input_json = request.json
        Brevet.objects.get(id=id).update(**input_json)
        return '', 200

    def delete(self, id):
        Brevet.objects.get(id=id).delete()
        return '', 200
