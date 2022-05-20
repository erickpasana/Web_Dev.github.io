# ---- Flask Hello World ---- #
# import the Flask class from the flask package
from flask import Flask
# import numpy as np

# create the application object
app = Flask(__name__)
# use the decorator pattern to
# link the view function to a url
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return "Hello World! My 1st Web Application!"
    # start the development server using the run() method

# dynamic route
@app.route("/test/<query>")
def search(query):
    return query
# def search():
#     return "Hello dynamic!"

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"
@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1.0)
    return "correct"
# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

if __name__ == "__main__":
    app.run()