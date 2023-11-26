from flask import Flask, jsonify,request
import ipl

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

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
