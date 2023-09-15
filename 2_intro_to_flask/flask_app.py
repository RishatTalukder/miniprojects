# importing flask
from flask import Flask, render_template

# creatign a flas app instance
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/layout")
# def layout():
#     return render_template("layout.html")


# defining a route
# @app.route("/")
# def home():
#     return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
