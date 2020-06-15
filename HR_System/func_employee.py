import json
from Load_Data import employee as el
from HR_System import func_role as fr
from HR_System import func_team as ft

dataemp = el.load_employee_data()

def view_emp(userdata):
    if userdata['role_id'] == 1:
        #1 = employee
        print_data_emp(userdata)
    elif userdata['role_id'] == 2:
        #2 = manager
        for emp in dataemp['employees']:
            if emp['team_id'] == userdata['team_id']:
                print_data_emp(emp)
    elif userdata['role_id'] == 3:
        #3 = admin
        for emp in dataemp['employees']:
            print_data_emp(emp)

def print_data_emp(userdata):
    print("\n-----------------------------------------------------------")
    print("Employee ID : " + str(userdata['emp_id']))
    print("Name : " + userdata['name'])
    print("E-mail : " + userdata['email'])
    print("Password : " + userdata['password'])
    rolename = fr.get_role_name(userdata['role_id'])
    print("Role : " + rolename)
    teamname = ft.get_team_name(userdata['team_id'])
    print("Team : " + teamname)
    status = check_employee_status(userdata['status_id'])
    print("Status : " + status)
    print("Leave Balance : " + str(userdata['leave']))
    print("-----------------------------------------------------------\n")


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
    print("Added Successfully!")

def check_employee_status(status):
    if status == 0:
        return "Probation"
    elif status == 1:
        return "Permanent"
    elif status ==2:
        return "Resigned"