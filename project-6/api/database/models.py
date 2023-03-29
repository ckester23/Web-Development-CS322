"""
Credit: I Copied and modified the models from ToDoListRESTful
"""
from mongoengine import *


class Checkpoint(EmbeddedDocument):
  """
  A MongoEngine EmbeddedDocument containing:
      distance: MongoEngine float field, required, (checkpoint distance in kilometers),
      location: MongoEngine string field, optional, (checkpoint location name),
      open_time: MongoEngine datetime field, required, (checkpoint opening time),
      close_time: MongoEngine datetime field, required, (checkpoint closing time).
  """
  km = FloatField()
  miles = FloatField() # added for HTML simplicity
  location = StringField()

  # I set these as StringFields instead of DateField because Javascript
  # didn't like the date version
  open = StringField()
  close = StringField()
  

class Brevet(Document):
  """
  A MongoEngine document containing:
    length: MongoEngine float field, required
    start_time: MongoEngine datetime field, required
    checkpoints: MongoEngine list field of Checkpoints, required
  """
  length = FloatField()
  start_time = StringField()

  # We use EmbeddedDocumentListField here because Checkpoint inherits it
  checkpoints = EmbeddedDocumentListField(Checkpoint)
