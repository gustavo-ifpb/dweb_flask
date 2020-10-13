from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired

class SignInForm(FlaskForm):
  
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])


class SignUpForm(FlaskForm):
  
  name = StringField('Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  photo = FileField(validators=[FileRequired()])
  is_admin = BooleanField('Admin', validators=[DataRequired()])