from flask import Flask, render_template, url_for
app = Flask(__name__)

questions = [
    "Are you willing to support your club for the rest of your days?",
    "Are you willing to support your club even if they never win any titles?",
    "Are you willing to support your club even if they don't have stars on the team?",
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/survey")
def survey():
    return render_template("survey.html", questions = questions)

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug = True)