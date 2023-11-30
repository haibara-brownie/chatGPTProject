from flask import Flask

app = Flask(__name__)


@app.route("/")
def x1():
    return "hellow world"


@app.route("/a")
def x2():
    return "<h1>hellow world</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=9000)