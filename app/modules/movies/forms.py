from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
  
  name = StringField('Name', validators=[DataRequired()])
  category = SelectField('Categoria', coerce=int)