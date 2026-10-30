from flask import Flask , render_template ,redirect ,url_for ,request

app = Flask(__name__)

@app.route("/")
def hello() :
    return "hello world"

@app.route("/name")
def name() :
    return "hello najad"

def name_1() :
    return "hello QUEST"
app.add_url_rule("/wel", "wel",name_1)

# -------------------------------------------------

@app.route("/name_1/<string:a>")
def name_1(a) :
    return "hello %s" %a

@app.route("/name_1/<int:a>")
def age(a) :
    return "my age : %d" %a

@app.route("/name_1/<float:a>")
def sal(a) :
    return "my salary : %f" %a

@app.route("/name_2")
def show() :
    return "<h1> welcome to najad </h1>"

@app.route("/name_2/<b>")
def show_1(b) :
    return "<h1> welcome to quest %s </h1>" %b
# ------------------------------------------------------------------
@app.route("/name_3/<b>")
def show_3(b) :
    return render_template('hello.html' , n=b)

@app.route("/show_4/<b>")
def show_4(b) :
    return render_template('hello_1.html' , n=b)

# -------------------------------------------------------------------

# ===================== ADDING REDIRECT PAGE ========================
@app.route("/admin/",endpoint="hello_admin")
def show_5() :
    return "<h1> welcome to admin </h1>"

@app.route("/staf/<a>", endpoint="staf")
def show_5(a) :
    return "<h1> welcome to %s </h1>" %a

@app.route("/user/<b>")
def show_5(b) :
    if b == "admin" :
        return redirect(url_for("hello_admin"))
    else :
        return redirect(url_for("staf" , a=b))
# -----------------------------------------------------------------

# =======================SENDING DATA FROM HTML PAGE==============================

@app.route("/data" , methods=['GET' , 'POST'])
def data():
    if request.method == 'POST' :
        name = request.form['name']
        age = request.form['age']
        place = request.form['place']
        return f'Name : {name} \n Age : {age} \n place : {place}'
    return render_template("data.html")

# --------------------------------------------------------------------------------

# =========================== DATABASE OPERATIONS===============================

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'

db = SQLAlchemy(app)

class Student(db.Model) :
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    course = db.Column(db.String(100))
with app.app_context() :
    db.create_all()    
# -------------------------------------------------------

@app.route('/reg')
def new_stud():
    return render_template('student1.html')

@app.route('/add', methods=['POST'])
def add_stud():
    id1 = request.form['id']
    nm = request.form['name']
    a = request.form['age']
    co= request.form['course']

    student = Student(id=id1, name=nm, age=a , course=co)

    db.session.add(student)
    db.session.commit()

    return "saved"

#------------------SHOWING DATA FROM DATABASE---------------------
@app.route('/show')
def show_stud():
    students = Student.query.all()
    return render_template('show.html', students=students)


#------------------UPDATING DATA FROM DATABASE---------------------
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_stud(id):
    student = Student.query.get(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.age = request.form['age']
        student.course = request.form['course']
        db.session.commit()
        return redirect(url_for('show_stud'))
    return render_template('update.html', students=student)

#------------------DELETING DATA FROM DATABASE---------------------
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_stud(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('show_stud'))

========================================================================/
    
# ------------------------------------------------------------------
if __name__ == "__main__" :
    app.run(debug = True)