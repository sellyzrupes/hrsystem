from Load_Data import load_role as lr
from Models import role as r

datarole = lr.load_role_data()
roles = r.Role.parse_from_dictionary(datarole)

def get_role_name(role_id):
    for role in roles:
        if role_id == role.role_id:
            return role.role_name

def print_all_role_name():
    for role in roles:
        print(str(role.role_id) + ". " + role.role_name)