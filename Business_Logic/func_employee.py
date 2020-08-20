import json
import config_variables as cv
from Load_Data import employee as el
from Business_Logic import func_role as fr
from Business_Logic import func_team as ft
from Models import employee as e

empdata = el.load_employee_data()
employees = e.Employee.parse_from_dictionary(empdata)

def view_emp(userdata):
    if userdata.role_id == 1:
        #1 = employee
        writedata = {
            "employees": e.Employee.get_employees_dict(userdata)
        }
        return writedata
    elif userdata.role_id == 2:
        #2 = manager
        temp = []
        for employee in employees:
            if employee.team_id == userdata.team_id:
                temp.append(employee.get_employees_dict())
        writedata = {
            "employees": temp
        }
        return json.dumps(writedata)
    elif userdata.role_id == 3:
        #3 = admin
        return empdata

def print_data_emp(userdata):
    print("\n-----------------------------------------------------------")
    print("Employee ID : " + str(userdata.emp_id))
    print("Name : " + userdata.name)
    print("E-mail : " + userdata.email)
    print("Password : " + userdata.password)
    #to get role name from role id
    rolename = fr.get_role_name(userdata.role_id)
    print("Role : " + rolename)
    #to get team name from team id
    teamname = ft.get_team_name(userdata.team_id)
    print("Team : " + teamname)
    status = check_employee_status(userdata.status_id)
    print("Status : " + status)
    print("Leave Balance : " + str(userdata.leave))
    print("-----------------------------------------------------------\n")

def check_employee_status(status):
    for key in cv.EMPLOYEE_STATUS.keys():
        if cv.EMPLOYEE_STATUS[key] == status:
            return key