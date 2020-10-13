# Import flask and template operators
from flask import Flask, render_template

# Import Peewee
from config import DATABASE
from peewee import SqliteDatabase


# Define the WSGI application object
app = Flask(__name__)

# CSRF
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
csrf.init_app(app)


# Configurations
app.config.from_object('config')


# Define the database object which is imported
# by modules and controllers
db = SqliteDatabase(DATABASE)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404



@app.before_request
def before_request():
  db.connect()

@app.after_request
def after_request(response):
  db.close()
  return response


# Blueprint
# Import a module / component using its blueprint handler variable (mod_auth)
from app.modules.core.controllers import blueprint as blueprint_core
from app.modules.users.controllers import blueprint as blueprint_users
from app.modules.categories.controllers import blueprint as blueprint_categories
from app.modules.movies.controllers import blueprint as blueprint_movies

# Register blueprint(s)
app.register_blueprint(blueprint_core)
app.register_blueprint(blueprint_users)
app.register_blueprint(blueprint_categories)
app.register_blueprint(blueprint_movies)


# Database:
from app.modules.users.models import User
from app.modules.categories.models import MovieCategory
from app.modules.movies.models import Movie

# This will create the database file
db.create_tables([User, MovieCategory, Movie])