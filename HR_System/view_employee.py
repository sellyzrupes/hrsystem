import json
from Load_Data import employee as el

dataemp = el.load_employee_data()

def view_emp(userdata):
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

def add_emp(inputname, inputemail, inputpass, inputrole,inputteam):
    l = len(dataemp['employees'])-1
    empid = int(dataemp['employees'][l]['emp_id'])+1
    newdata = {
        "emp_id": empid,
        "name": inputname,
        "email": inputemail,
        "password": inputpass,
        "role_id": int(inputrole),
        "team_id": int(inputteam),
        "status_id": 1,
        "leave": 14
    } 
    dataemp['employees'].append(newdata)
    with open('Database/employee.json','w') as emp2:
        json.dump(dataemp, emp2, indent=2)