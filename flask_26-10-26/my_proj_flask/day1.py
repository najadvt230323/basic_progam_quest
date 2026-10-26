from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello() :
    return "hello world"

@app.route("/name")
def name() :
    return "hello najad"




if __name__ == "__main__" :
    app.run(debug = True)