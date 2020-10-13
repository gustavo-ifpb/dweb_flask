import peewee
from app.modules.core import models as core
from app.modules.categories import models as categories


'''
class: Movie
'''
class Movie(core.BaseModel):

  name = peewee.CharField(unique=True)
  category = peewee.ForeignKeyField(categories.MovieCategory, backref='movies')