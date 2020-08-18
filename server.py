from Load_Data import employee as el
from Models import employee as e
from Business_Logic import func_employee as fe
from Business_Logic import func_leave as fl
from Business_Logic import func_team as ft
from Business_Logic import func_role as fr
from flask import Flask, request, abort
import json
import config_variables

app = Flask(__name__)

#@app.route('/login', methods=['POST'])
#def login(user,passwd):
#    if request.method == 'POST':
#        try:
#            empdata = el.load_employee_data()
#            employees = e.Employee.parse_from_dictionary(empdata)
#            for employee in employees:
#                if employee.email == user:
#                    if str(employee.password) == passwd:
#                        print("Login Success!")
#                        return employee
#                    else:
#                        return False
#        except IOError:
#            return 'Failed to connect to Db. Please contact admin.', 500
#        except ValueError as e:
#            return 'Failed to read Users Db. Please contact admin.', 500
#        finally:
#            f.close()
#    else:
#        abort(405)

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
                        return 'Login successful', 200
                    elif req_dct.get('password'):
                        return 'Wrong password entered' , 200
                    else:
                        return 'No password entered', 200

            return 'Login unsuccessful', 200
        except IOError:
            return 'Failed to connect to Db. Please contact admin.', 500
        except ValueError as ve:
            return 'Failed to read Users Db. Please contact admin.', 500
    else:
        abort(405)