import peewee
from flask import Blueprint, render_template, request, redirect, url_for



blueprint = Blueprint('core', __name__, url_prefix='/')


@blueprint.route('/', methods=['GET'])
def index():
  return render_template('core/index.html')