from flask import Flask , render_template ,redirect ,url_for

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
    if req
















    
# ------------------------------------------------------------------
if __name__ == "__main__" :
    app.run(debug = True)