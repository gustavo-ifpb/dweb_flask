import peewee, os, base64
from app import app
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename

from .models import User
from .forms import SignInForm, SignUpForm


blueprint = Blueprint('users', __name__, url_prefix='/users')


# Set the route and accepted methods
@blueprint.route('/login', methods=['GET', 'POST'])
def login():
  form = SignInForm(request.form)
  if request.method == 'GET':
    return render_template('users/login.html', form=form)
  else:
    if form.validate_on_submit():
      try:
        user = User.get(email=form.email.data, password=form.password.data)
        print(user.photo)
        if user:
          session['user_id'] = user.id
          session['name'] = user.name
          session['email'] = user.email
          session['photo'] = user.photo
        else:
          return render_template('users/login.html', error='Email ou senha incorretos!', form=form)
      except peewee.IntegrityError:
        return render_template('users/login.html', error='Email ou senha incorretos!', form=form)
      return redirect(url_for('movies.index'))

    return render_template('users/login.html', form=form)


# Set the route and accepted methods
@blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignUpForm()
  if request.method == 'GET':
    return render_template('users/signup.html', form=form)
  else:
    if form.validate_on_submit():
      try:
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(path)
        
        user = User.create(name=form.name.data, email=form.email.data, password=form.password.data, photo=filename, is_admin=form.is_admin.data)
        session['user_id'] = user.id
        session['name'] = user.name
        session['email'] = user.email
        session['photo'] = filename
      except peewee.IntegrityError:
        return render_template('users/signup.html', error='Usuário já cadastrado!', form=form)
      return redirect(url_for('movies.index'))
    return render_template('users/signup.html', form=form)

@blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
  session.pop('user_id', None)
  session.pop('name', None)
  session.pop('email', None)
  session.pop('photo', None)
  return redirect(url_for('movies.index'))


@blueprint.route('/images/')
def photo():
  return redirect(url_for('static', filename=f'uploads/{session["photo"]}'), code=301)