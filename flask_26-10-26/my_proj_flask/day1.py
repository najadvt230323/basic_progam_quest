from flask import Flask

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




# ------------------------------------------------------------------
if __name__ == "__main__" :
    app.run(debug = True)