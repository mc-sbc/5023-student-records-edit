from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, SelectField
from wtforms.validators import InputRequired

class AddStudentForm(FlaskForm):
    name = StringField('Student name', validators=[InputRequired()])
    grade_id = SelectField('Grade', coerce=int)
    house_id = SelectField('House')
    english_mark = IntegerField('English', validators=[InputRequired()])
    science_mark = IntegerField('Science', validators=[InputRequired()])
    mathematics_mark = IntegerField('Mathematics', validators=[InputRequired()])
    does_homework = BooleanField('Does homework?')
    stays_on_task = BooleanField('Stays on task?')
    
    submit = SubmitField('Add student')

# TODO: Add a form for editing the student (called EditStudentForm), which inherits from AddStudentForm
class EditStudentForm(AddStudentForm):
    submit = SubmitField('Save changes')

class AddGradeForm(FlaskForm):
    name = StringField('Grade name', validators=[InputRequired()])
    submit = SubmitField('Add grade')

class EditGradeForm(AddGradeForm):
    submit = SubmitField('Save changes')

class AddHouseForm(FlaskForm):
    colour = StringField('Colour', validators=[InputRequired()])
    active = BooleanField('Active?')
    submit = SubmitField('Add house')

class EditHouseForm(AddHouseForm):
    submit = SubmitField('Save changes')
