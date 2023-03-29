"""
Contains two database interaction functions for flask_brevets
"""
import os
from pymongo import MongoClient
import arrow
import sys

# set up mongo connection
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
# use brevets database
db = client.brevets
# use tables collection
collection = db.tables

## Database Interaction functions ##

def brevet_insert(brevet_dist, start_time, checkpoints):
    """
    Inserts a new table into the database "brevets", under the collection "tables".
    Inputs a brevet (string), a start time (string), and checkpoints (list of dictionaries)

    Returns the unique ID assigned to the document by mongo (primary key)

    This is copied from ToDoListApp and modified 
    """
    output = collection.insert_one({
        "brevet": brevet_dist,
        "start": start_time,
        "checkpoints": checkpoints})

    _id = output.inserted_id # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)

def brevet_find():
    """
    Obtains the newest document in the "tables" collection in database "brevets".

    Returns brevet (string), start time(string), and checkpoints (list of dictionaries)
    as a tuple.

    This is copied from ToDoListApp and modified 
    """
    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.

    lists = collection.find().sort("_id", -1).limit(1)

    # lists is a PyMongo cursor, which acts like a pointer.
    # We need to iterate through it, even if we know it has only one entry:
    for table in lists:
        # We store all of our lists as documents with three fields:
        ## brevet: string # brevet value in km
        ## start: formatted string # start time
        ## checkpoints: list  # list of checkpoint dictionaries:

        ### every checkpoint has five fields:
        #### km: int   # checkpoint dist in km
        #### miles: int  # checkpoint dist in miles
        #### open: formatted string # open time for the checkpoint
        #### close: formatted string # close time for the checkpoint
        #### location: string # (Optional) Location of the checkpoint
        return table["brevet"], table["start"], table["checkpoints"]
        
## ##
