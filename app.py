from flask import Flask, jsonify,request,render_template,redirect
import ipl
from database import Database
dbo = Database()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")



@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/perform_registration", methods=['post'])
def perform_registration():
    email = request.form.get('user_ka_email')
    name = request.form.get("user_ka_name")
    password = request.form.get('user_ka_password')
    response = dbo.insert(name,email,password)
    if(response == 1):
        return render_template("Login.html",message='Registration Successful. Kindly Login to procced')
    else:
        return render_template("register.html", message="Email already Exists")

@ app.route("/perform_login", methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')
    response = dbo.search(email,password)
    if response == 1:
        return redirect("/use_api")
    else:
        return render_template("login.html",message="incorrect email/password")

@app.route("/use_api")
def use_api():
    return render_template("useAPI.html")
@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)

@app.route('/api/teamVteam')
def teamVteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.teamVteamAPI(team1,team2)
    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = ipl.teamAPI(team_name)
    return jsonify(response)

@app.route('/api/batter')
def batter():
    batsman = request.args.get('batsman')
    response = ipl.batterAPI(batsman)
    return jsonify(response)

app.run(debug=True)
