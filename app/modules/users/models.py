import peewee
from app.modules.core import models as core


'''
class: User
'''
class User(core.BaseModel):

  name = peewee.CharField()
  email = peewee.CharField(unique=True)
  password = peewee.CharField()
  photo = peewee.CharField()