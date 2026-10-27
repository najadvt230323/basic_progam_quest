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


if __name__ == "__main__" :
    app.run(debug = True)