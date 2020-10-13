# # Import flask dependencies
import peewee
from flask import Blueprint, render_template, request, redirect, url_for

# Import module models (i.e. User)
from .models import MovieCategory
from .forms import CategoryForm


# Define the blueprint: 'categories', set its url prefix: app.url/categories
blueprint = Blueprint('categories', __name__, url_prefix='/categories')


# ~~~~~~~~~~~~~
@blueprint.route('/', methods=['GET'])
def index():
  categories = MovieCategory.select().order_by(MovieCategory.name.desc())

  return render_template('categories/list.html', categories=categories)


# ~~~~~~~~~~~~~
@blueprint.route('/detail/<int:category_id>', methods=['GET'])
def detail(category_id):
  category = MovieCategory.get(id=category_id)

  return render_template('categories/detail.html', category=category)


# ~~~~~~~~~~~~~
@blueprint.route('/create', methods=['GET'])
def formGet():
  form = CategoryForm(request.form)
  return render_template('categories/form.html', form=form)


@blueprint.route('/create', methods=['POST'])
def formPost():
  form = CategoryForm(request.form)
  if form.validate_on_submit():

    try:
      MovieCategory.create(name=form.name.data)
    except peewee.IntegrityError:
      return render_template('categories/form.html', error='Categoria já cadastrada!', form=form)

    return redirect(url_for('categories.index'))

  return render_template('categories/form.html', form=form)


# ~~~~~~~~~~~~~
@blueprint.route('/update/<int:category_id>', methods=['GET', 'POST'])
def formUpdate(category_id):
  category = MovieCategory.get(id=category_id)
  form = CategoryForm(request.form, obj=category)

  if request.method == 'GET':
    return render_template('categories/update.html', category=category, form=form)

  else:
    if request.form['name']:

      try:
        category.name = request.form['name']
        category.save()
      except peewee.IntegrityError:
        return render_template('categories/update.html', category=category, error='Categoria já cadastrada!', form=form)

      return redirect(url_for('categories.index'))
      
    return render_template('categories/update.html', category=category, form=form)