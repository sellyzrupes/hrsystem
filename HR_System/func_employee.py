import json
from Load_Data import employee as el
from HR_System import func_role as fr
from HR_System import func_team as ft
from Models import employee as e

empdata = el.load_employee_data()
employees = e.Employee.parse_from_dictionary(empdata)

def view_emp(userdata):
    if userdata.role_id == 1:
        #1 = employee
        print_data_emp(userdata)
    elif userdata.role_id == 2:
        #2 = manager
        for employee in employees:
            if employee.team_id == userdata.team_id:
                print_data_emp(employee)
    elif userdata.role_id == 3:
        #3 = admin
        for employee in employees:
            print_data_emp(employee)

def print_data_emp(userdata):
    print("\n-----------------------------------------------------------")
    print("Employee ID : " + str(userdata.emp_id))
    print("Name : " + userdata.name)
    print("E-mail : " + userdata.email)
    print("Password : " + userdata.password)
    rolename = fr.get_role_name(userdata.role_id)
    print("Role : " + rolename)
    teamname = ft.get_team_name(userdata.team_id)
    print("Team : " + teamname)
    status = check_employee_status(userdata.status_id)
    print("Status : " + status)
    print("Leave Balance : " + str(userdata.leave))
    print("-----------------------------------------------------------\n")


def add_emp(inputname, inputemail, inputpass, inputrole,inputteam):
    l = len(employees)-1
    newid = int(employees[l].emp_id)+1
    newdata = e.Employee(newid, inputname, inputemail, inputpass, int(inputrole), int(inputteam), 1, 14)
    # {
    #     "emp_id": empid,
    #     "name": inputname,
    #     "email": inputemail,
    #     "password": inputpass,
    #     "role_id": int(inputrole),
    #     "team_id": int(inputteam),
    #     "status_id": 1,
    #     "leave": 14
    # } 
    employees.append(newdata)
    with open('Database/employee.json','w') as emp_file:
        json.dump(employees, emp_file, indent=4)
    print("Added Successfully!")

def check_employee_status(status):
    if status == 0:
        return "Probation"
    elif status == 1:
        return "Permanent"
    elif status ==2:
        return "Resigned"