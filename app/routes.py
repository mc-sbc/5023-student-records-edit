from flask import render_template, redirect, url_for

from app import app, db
from app.models import Student, Grade, House
from app.forms import AddHouseForm, AddStudentForm, AddGradeForm, EditGradeForm, EditHouseForm, EditStudentForm

@app.route('/')
def index():
    # Load the students from the database file for the table
    students = Student.query.all()
    # Return the index view with the list of students for display
    return render_template('index.html', students = students)

@app.route('/student/add', methods = ['GET', 'POST'])
def student_add():
    form = AddStudentForm()
    form.grade_id.choices = [(grade.id, grade.name) for grade in Grade.query.all()]
    form.house_id.choices = [(house.id, house.colour) for house in House.query.all()]

    # Check if the form has been submitted (is a POST request) and form inputs are valid
    if form.validate_on_submit():
        # Get data from the form and put in a Student object, save new Student to database
        student = Student()
        form.populate_obj(obj=student)
        db.session.add(student)
        db.session.commit()
        
        # Returns the view with the list of students, with the new student added
        return redirect(url_for('index'))

    # When there is a GET request, the view with the form is returned
    return render_template('student_add.html', form = form)

@app.route('/student/<int:id>')
def student_details(id):
    student = Student.query.get_or_404(id)
    return render_template('student_details.html', student = student)

@app.route('/student/<int:id>/edit', methods = ['GET', 'POST'])
def student_edit(id):
    student = Student.query.get_or_404(id)
    form = EditStudentForm(obj=student)
    form.grade_id.choices = [(grade.id, grade.name) for grade in Grade.query.all()]
    form.house_id.choices = [(house.id, house.colour) for house in House.query.all()]

    if form.validate_on_submit():
        form.populate_obj(obj=student)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('student_edit.html', form = form, student = student)

@app.route('/student/<int:id>/delete')
def student_delete(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/grade')
def grade_list():
    grades = Grade.query.all()
    return render_template('grade_list.html', grades = grades)

@app.route('/grade/add', methods = ['GET', 'POST'])
def grade_add():
    form = AddGradeForm()
    # Check if the form has been submitted, and processed with no errors
    if form.validate_on_submit():
        # Put the form inputs into the new Grade record and save this to db
        grade = Grade()
        form.populate_obj(obj=grade)
        db.session.add(grade)
        db.session.commit()
        # The adding of the grade has been successful, return to the list of grades
        return redirect(url_for('grade_list'))
    
    # If there is a GET request or there are form errors, return the view with the form
    return render_template('grade_add.html', form = form)

@app.route('/grade/<int:id>/edit', methods = ['GET', 'POST'])
def grade_edit(id):
    # Retrieve the grade for the given id from the database, and fill in form from grade
    grade = Grade.query.get_or_404(id)
    form = EditGradeForm(obj=grade)

    # If the form has been submitted and there are no errors, update and save the Grade record
    if form.validate_on_submit():
        form.populate_obj(obj=grade)
        db.session.commit()
        return redirect(url_for('grade_list'))

    # If the request is a GET or there are errors in the form inputs, return the view with the form
    return render_template('grade_edit.html', form = form, grade = grade)

@app.route('/grade/<int:id>/delete')
def grade_delete(id):
    # Retrieve and delete the Grade record for the given id
    grade = Grade.query.get_or_404(id)
    db.session.delete(grade)
    db.session.commit()
    return redirect(url_for('grade_list'))

@app.route('/house')
def house_list():
    houses = House.query.all()
    return render_template('house_list.html', houses = houses)

@app.route('/house/add', methods = ['GET', 'POST'])
def house_add():
    form = AddHouseForm()
    # Check if the form has been submitted, and processed with no errors
    if form.validate_on_submit():
        # Put the form inputs into the new House record and save this to db
        house = House()
        form.populate_obj(obj=house)
        db.session.add(house)
        db.session.commit()
        # The adding of the house has been successful, return to the list of houses
        return redirect(url_for('house_list'))
    
    # If there is a GET request or there are form errors, return the view with the form
    return render_template('house_add.html', form = form)

@app.route('/house/<int:id>/edit', methods = ['GET', 'POST'])
def house_edit(id):
    # Retrieve the house for the given id from the database, and fill in form from house
    house = House.query.get_or_404(id)
    form = EditHouseForm(obj=house)

    # If the form has been submitted and there are no errors, update and save the House record
    if form.validate_on_submit():
        form.populate_obj(obj=house)
        db.session.commit()
        return redirect(url_for('house_list'))

    # If the request is a GET or there are errors in the form inputs, return the view with the form
    return render_template('house_edit.html', form = form, house = house)

@app.route('/house/<int:id>/delete')
def house_delete(id):
    # Retrieve and delete the House record for the given id
    house = House.query.get_or_404(id)
    db.session.delete(house)
    db.session.commit()
    return redirect(url_for('house_list'))