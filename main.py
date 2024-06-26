
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/concepts")
def concepts():
    return render_template("concepts.html")

@app.route("/applications")
def applications():
    return render_template("applications.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

if __name__ == "__main__":
    app.run(debug=True)
