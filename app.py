from flask import Flask
from flask import render_template

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def layout():
    return render_template("index.html")

@app.route("/about")
def about():
    render_template("about.html")