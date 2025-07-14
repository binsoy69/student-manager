from flask import Flask, render_template, request, redirect, url_for
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



@app.route('/')
def home():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    fullname = request.form['fullname']
    email = request.form['email']
    course = request.form['course']
    
    new_student = Student(fullname=fullname, email=email, course=course)
    db.session.add(new_student)
    db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
