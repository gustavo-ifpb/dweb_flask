# # Import flask dependencies
from flask import Blueprint, render_template

# Import module models (i.e. User)
from .models import MovieCategory

# Define the blueprint: 'categories', set its url prefix: app.url/categories
blueprint = Blueprint('categories', __name__, url_prefix='/categories')


# Set the route and accepted methods
@blueprint.route('/', methods=['GET'])
def index():
  category, created = MovieCategory.get_or_create(name='Terror')

  return render_template('categories/index.html', category=category)


@blueprint.route('/list', methods=['GET'])
def list():
  categories = MovieCategory.select().order_by(MovieCategory.name.desc())

  return render_template('categories/list.html', categories=categories)