from Load_Data import employee as el
from Models import employee as e
from Business_Logic import func_employee as fe
from Business_Logic import func_leave as fl
from Business_Logic import func_team as ft
from Business_Logic import func_role as fr
from flask import Flask, request, abort, make_response
import json
import config_variables
import crypt

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            empdata = el.load_employee_data()
            employees = e.Employee.parse_from_dictionary(empdata)
            req_dct = request.get_json()

            # Login user
            for employee in employees:
                if req_dct.get('email') == employee.email:
                    if req_dct.get('password') == employee.password:
                        # Redirect
                        resp = make_response(e.Employee.get_employees_dict(employee), 200)
                        resp.set_cookie("login_token", config_variables.SECRET_KEY)
                        return resp
                    elif req_dct.get('password'):
                        return make_response('Wrong password entered' , 200)
                    else:
                        return make_response('No password entered', 200)

            return make_response('Login unsuccessful', 200)
        except IOError:
            return make_response ('Failed to connect to Db. Please contact admin.', 500)
        except ValueError as ve:
            return make_response('Failed to read Users Db. Please contact admin.', 500)
    else:
        abort(405)

@app.route('/view_employee', methods=['GET'])
def view_employee():
    if request.method == 'GET':
        try:
            emp_id = request.args.get('emp_id')
            empdata = el.load_employee_data()
            employees = e.Employee.parse_from_dictionary(empdata)
            encrypted_token = request.cookies.get('login_token')
            if encrypted_token:
                for employee in employees:
                    if int(emp_id) == employee.emp_id:
                        result = fe.view_emp(employee)
                        return make_response(result, 200)
            else:
                return make_response('View employee data unsuccessful', 200)
        except IOError:
            return make_response('Failed to connect to Db. Please contact admin.', 500)
        except ValueError as ve:
            return make_response('Failed to read Users Db. Please contact admin.', 500)
    else:
        abort(405)

@app.route('/apply_leave', methods=['POST'])
def apply_leave():
    if request.method == 'POST':
        try:
            empdata = el.load_employee_data()
            employees = e.Employee.parse_from_dictionary(empdata)
            req_dct = request.get_json()
        except IOError:
            return make_response('Failed to connect to Db. Please contact admin.', 500)
        except ValueError as ve:
            return make_response('Failed to read Users Db. Please contact admin.', 500)
    else:
        abort(405)