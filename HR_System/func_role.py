import json
from Load_Data import load_role as lr

datarole = lr.load_role_data()

def get_role_name(role_id):
    for val in datarole:
        if role_id == val['role_id']:
            return val['role_name']

def print_all_role_name():
    for val in datarole:
        print(str(val['role_id']) + ". " + val['role_name'])