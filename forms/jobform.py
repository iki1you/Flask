from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = StringField('Team Leader', validators=[DataRequired()])
    job = StringField('Job Title', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?')
    work_size = IntegerField('Work Size', validators=[DataRequired()])
    submit = SubmitField('Войти')
