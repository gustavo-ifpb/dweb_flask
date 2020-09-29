# # Import flask dependencies
import peewee
from flask import Blueprint, render_template, request, redirect, url_for

# Import module models (i.e. User)
from .models import MovieCategory



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
  return render_template('categories/form.html')



@blueprint.route('/create', methods=['POST'])
def formPost():
  if request.form['name']:
    
    try:
      MovieCategory.create(name=request.form['name'])
    except peewee.IntegrityError:
      return render_template('categories/form.html', error='Categoria já cadastrada!')

    return redirect(url_for('categories.index'))

  return render_template('categories/form.html')






# ~~~~~~~~~~~~~
@blueprint.route('/update/<int:category_id>', methods=['GET', 'POST'])
def formUpdate(category_id):
  category = MovieCategory.get(id=category_id)

  if request.method == 'GET':
    return render_template('categories/update.html', category=category)

  else:
    if request.form['name']:

      try:
        category.name = request.form['name']
        category.save()
      except peewee.IntegrityError:
        return render_template('categories/update.html', category=category, error='Categoria já cadastrada!')

      return redirect(url_for('categories.index'))
      
    return render_template('categories/update.html', category=category)