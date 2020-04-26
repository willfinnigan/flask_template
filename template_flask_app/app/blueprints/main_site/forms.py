from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class AForm(FlaskForm):
    string = StringField('String', validators=[DataRequired()])
    submit = SubmitField('Start')