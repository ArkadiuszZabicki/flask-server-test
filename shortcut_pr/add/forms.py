from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class UserInputForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()], choices=[
        ('income', 'income'), ('expenses', 'expenses')])
    category = SelectField('Type', validators=[DataRequired()], choices=[
        ('rent', 'rent'), ('salary', 'salary'), ('investment', 'investment'), ('hooking', 'hooking')])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add new values')
