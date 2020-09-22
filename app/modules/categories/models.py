import peewee
from app.modules.core import models as core


'''
class: Movie Category
'''
class MovieCategory(core.BaseModel):

  name = peewee.CharField(unique=True)