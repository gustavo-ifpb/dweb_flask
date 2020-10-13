# # Import flask dependencies
import peewee
from flask import Blueprint, render_template, request, redirect, url_for

# Import module models (i.e. User)
from .models import Movie
from .forms import MovieForm

from app.modules.categories.models import MovieCategory


# Define the blueprint: 'categories', set its url prefix: app.url/categories
blueprint = Blueprint('movies', __name__, url_prefix='/movies')




# ~~~~~~~~~~~~~
@blueprint.route('/', methods=['GET'])
def index():
  movies = Movie.select().order_by(Movie.name)

  return render_template('movies/list.html', movies=movies)


# ~~~~~~~~~~~~~
@blueprint.route('/detail/<int:movie_id>', methods=['GET'])
def detail(movie_id):
  movie = Movie.get(id=movie_id)

  return render_template('movies/detail.html', movie=movie)


# ~~~~~~~~~~~~~
@blueprint.route('/create', methods=['GET', 'POST'])
def formCreate():
  categories = [(b.id, b.name) for b in MovieCategory.select()]

  form = MovieForm(request.form)
  form.category.choices = categories

  if request.method == 'GET':
    return render_template('movies/form.html', form=form)

  else:
    if form.validate_on_submit():
      try:
        Movie.create(name=form.name.data, category=form.category.data)
      except peewee.IntegrityError:
        return render_template('movies/form.html', error='Filma já cadastrado!', form=form)

      return redirect(url_for('movies.index'))

    return render_template('movies/form.html', form=form)


# ~~~~~~~~~~~~~
@blueprint.route('/update/<int:movie_id>', methods=['GET', 'POST'])
def formUpdate(movie_id):
  movie = Movie.get(id=movie_id)
  categories = [(b.id, b.name) for b in MovieCategory.select()]

  form = MovieForm(request.form, obj=movie)
  form.category.choices = categories
  
  if request.method == 'GET':
    form.category.data = movie.category.id
    return render_template('movies/update.html', movie=movie, form=form)

  else:
    if form.validate_on_submit():
      try:
        movie.name = form.name.data
        movie.category = form.category.data
        movie.save()
      except peewee.IntegrityError:
        return render_template('movies/update.html', error='Filma já cadastrado!', form=form)

      return redirect(url_for('movies.index'))

    return render_template('movies/update.html', form=form, movie=movie)