from flask import Flask, render_template, url_for
import sqlite3
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
    club = getClub(None)
    return render_template("result.html", club = club)

def getClub(league):

    conn = sqlite3.connect("clubs.db")
    cur = conn.cursor()
    
    if (league):
        cur.execute("SELECT name FROM clubs WHERE league = ? ORDER BY RANDOM() LIMIT 1", (league,))
    else:
        cur.execute("SELECT name FROM clubs ORDER BY RANDOM() LIMIT 1")

    club = cur.fetchall()
    conn.close()
    
    return club[0][0]
    

if __name__ == "__main__":
    app.run(debug = True)