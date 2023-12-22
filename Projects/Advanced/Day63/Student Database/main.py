from flask import Flask, render_template, request, redirect, url_for,flash

#https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application


from flask_bootstrap import Bootstrap5

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String,DateTime
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired,Email,ValidationError


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
bootstrap=Bootstrap5(app)
db = SQLAlchemy()

# initialize the app with the extension
db.init_app(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created = db.Column(DateTime(timezone=True), default=func.now())


    
    def __repr__(self):
        return f'<Student {self.firstname}>'
    


class StudentForm(FlaskForm):

    name=StringField('First Name ',validators=[DataRequired()])
    surname=StringField('Last Name',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    age=IntegerField('Age',validators=[DataRequired()])

    #Custom validation below to make sure that user does not use the same email
    def validate_email(self, field):
        if Student.query.filter_by(email=field.data).first():
            raise ValidationError('Email already in use.')


    submit = SubmitField('Submit')

app.config['SECRET_KEY'] = 'MohauForms'

    
with app.app_context():
    db.create_all()



@app.route('/')
def index():
    all_students = Student.query.all()
    return render_template('index.html', students=all_students)



#Route and function to add form
@app.route("/add",methods=["POST","GET"])

def add_student():
    form=StudentForm()


    if form.validate_on_submit():
      

        all_student=Student (
            firstname=request.form['name'],
            lastname=request.form['surname'],
            email=request.form['email'],
            age=request.form['age']
        )
        db.session.add(all_student)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('add.html',form=form)

#Route and function to edit form, remember to pass form as a parameter when using,
#Flaskform
@app.route('/<int:student_id>/edit/', methods=('GET', 'POST'))
def edit(student_id):

    form=StudentForm()
    student = Student.query.get_or_404(student_id)
   

    if form.validate_on_submit():

        name_update = request.form['name']
        lastname_update = request.form['surname']
        age=request.form['age']

        student.firstname = name_update
        student.lastname = lastname_update
        student.age = age
     
   

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', student=student,form=form)


@app.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('student.html', student=student)


@app.route('/<int:student_id>/delete/',methods=('GET','POST'))
def delete(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    #parameters are defined for jinja
    #parameters are not declared i.e student =student because they were already declared
    #on def(index) route---so they already there for jinja to use
    return redirect(url_for('index'))


if __name__ == "__main__":

    app.run(debug=True)
