import json
from Load_Data import load_team as lt

datateam = lt.load_team_data()

def get_team_name(team_id):
    for val in datateam:
        if team_id == val['team_id']:
            return val['team_name']

def print_all_team_name():
    for val in datateam:
        print (str(val['team_id']) + ". " + val['team_name'])