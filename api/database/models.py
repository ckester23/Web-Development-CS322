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
  open = DateTimeField()
  close = DateTimeField()
  # open = DateTimeField()
  # close = DateTimeField()

class Brevet(Document):
  """
  A MongoEngine document containing:
  length: MongoEngine float field, required
  start_time: MongoEngine datetime field, required
  checkpoints: MongoEngine list field of Checkpoints, required
  """
  length = FloatField()
  start_time = DateTimeField()
  checkpoints = EmbeddedDocumentListField(Checkpoint)
