from flask import Flask

app = Flask(__name__)

@app.route("/")
def your_name():
    return "<p>Hello, Safayet!</p>"
