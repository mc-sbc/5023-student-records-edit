from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Turns this setting off, helps with performance
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'example-secret' #Used for demonstration, DO NOT use in production

db = SQLAlchemy(app)

from app import routes
from app.models import Student, Grade, House

@app.cli.command('init-db')
def create_db():
    # Recreate database for defined models
    db.drop_all()
    db.create_all()

    year4 = Grade(name='Year 4')
    db.session.add(year4)

    year5 = Grade(name='Year 5')
    db.session.add(year5)

    year6 = Grade(name='Year 6')
    db.session.add(year6)

    red = House(colour='Red', active=True)
    db.session.add(red)

    green = House(colour='Green', active=True)
    db.session.add(green)

    blue = House(colour='Blue', active=False)
    db.session.add(blue)

    # Creates two example students, we do not need to add these to the sessions explicitly
    # Flask-SQLAlchemy works out that they need to be added, as they are linked to the grade records above.
    jack = Student (
        name = 'Jack',
        grade = year6,
        house = red,
        english_mark = 90,
        science_mark = 90,
        mathematics_mark = 90,
        does_homework = True,
        stays_on_task = False
    )

    dom = Student (
        name = 'Dom',
        grade = year5,
        house = green,
        english_mark = 90,
        science_mark = 100,
        mathematics_mark = 90,
        does_homework = True,
        stays_on_task = True    
    )
    db.session.commit()


