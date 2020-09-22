from app import db
from peewee import Model


'''
class: Base Model
'''
class BaseModel(Model):

  class Meta:
    # Indica em qual banco de dados a tabela sera criada (obrigatorio). Neste caso, utilizamos o banco 'movies.db'
    database = db