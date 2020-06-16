from Load_Data import load_team as lt
from Models import team as t

datateam = lt.load_team_data()
teams = t.Team.parse_from_dictionary(datateam)

def get_team_name(team_id):
    for team in teams:
        if team_id == team.team_id:
            return team.team_name

def print_all_team_name():
    for team in teams:
        print (str(team.team_id) + ". " + team.team_name)