import peewee
from flask import Blueprint, render_template, request, redirect, url_for

from .models import User


blueprint = Blueprint('users', __name__, url_prefix='/users')


# Set the route and accepted methods
@blueprint.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('users/login.html')
  return render_template('categories/list.html', categories=categories)