from Load_Data import employee as el
from Models import employee as e
from Business_Logic import func_employee as fe
from Business_Logic import func_leave as fl
from Business_Logic import func_team as ft
from Business_Logic import func_role as fr
from flask import Flask, request, abort
import json
import config

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login(user,passwd):
    if request.method == 'POST':
        try:
            empdata = el.load_employee_data()
            employees = e.Employee.parse_from_dictionary(empdata)
            for employee in employees:
                if employee.email == user:
                    if str(employee.password) == passwd:
                        print("Login Success!")
                        return employee
                    else:
                        return False
