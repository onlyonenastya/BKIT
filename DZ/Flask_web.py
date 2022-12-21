from flask import Flask
from generator import fib
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/fibonachi")
def fibonachi_start():
    return "Write after URL '/number!'"

@app.route("/fibonachi/<int:n>")
def fibonachi_number(n):
    return list(fib(n))

@app.errorhandler(404)
def page_not_found(e):
    return "Oops! Try to enter a '/fibonachi/number!'"

if __name__ == "__main__":
    app.run()
