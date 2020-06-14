import json
from Load_Data import employee as el

def view_emp(userdata):
    dataemp = el.load_employee_data()
    if userdata['role_id'] == 1:
        #1 = employee
        print json.dumps(userdata, indent=2, sort_keys=True)
    elif userdata['role_id'] == 2:
        #2 = manager
        for emp in dataemp['employees']:
            if emp['team_id'] == userdata['team_id']:
                print json.dumps(emp, indent=2, sort_keys=True)
    elif userdata['role_id'] == 3:
        #3 = admin
        print json.dumps(dataemp, indent=2, sort_keys=True)