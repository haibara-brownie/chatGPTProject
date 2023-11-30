from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/login", methods=["get"])
def login():
    uname = request.values.get("uname")
    pwd = request.values.get("pwd")
    return f"收到了参数{uname} {pwd}"


@app.route("/")
def x1():
    return render_template("index.html")


@app.route("/a")
def x2():
    return "<h1>hellow world</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=9000)