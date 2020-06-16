from Load_Data import employee as el
from Models import employee as e
from Business_Logic import func_employee as fe
from Business_Logic import func_leave as fl
from Business_Logic import func_team as ft
from Business_Logic import func_role as fr

def main():
    #TODO: write the function to run the different options. Handle the case for various user_roles.
    login_option = True
    while login_option > 0:
        login_menu()
        login_option = get_option_input()
        # Main Menu: 1 = Login, 0 = Exit
        if (login_option == 1):
            user = raw_input("Input username/email: ")
            passwd = raw_input("Input password: ")
            userdata = login(user,passwd)
            if bool(userdata) == True:
                menu_option = True
                while menu_option > 0:
                    menu(userdata)
                    menu_option = get_option_input()
                    #0 = Logout
                    if(menu_option == 0):
                        logout()
                    # 1= View Employee
                    elif (menu_option == 1):
                        fe.view_emp(userdata)
                    #2 = Apply Leave
                    elif (menu_option == 2):
                        start_date = raw_input("Insert start date(format dd-mm-yyyy): ")
                        end_date = raw_input("Insert end date(format dd-mm-yyyy): ")
                        fl.apply_leave(start_date,end_date,userdata)
                    #3 = Approve Leave
                    elif (menu_option == 3):
                        pending_approval = fl.view_pending_leave(userdata)
                        if(pending_approval > 0):
                            inputapprove  = raw_input("Choose employee ID: ")
                            print("1. Approve\n2. Reject\n0.Cancel")
                            inputstatus = get_option_input()
                            if(inputstatus > 0):
                                fl.approve_leave(inputapprove, inputstatus)
                    #4 = Add Employee
                    elif (menu_option == 4):
                        inputname = raw_input("Insert name: ")
                        inputemail = raw_input("Insert email: ")
                        inputpass = raw_input("Insert password: ")
                        fr.print_all_role_name()
                        inputrole = raw_input("Insert role id: ")
                        ft.print_all_team_name()
                        inputteam = raw_input("Insert team id: ")
                        fe.add_emp(inputname, inputemail, inputpass, inputrole, inputteam)
                    else:
                        print("Invalid input!")
            else:
                print("Wrong input, please try again")
        elif (login_option == 10):
            print("Wrong input, please try again")
    print("The program will quit now.")

def login_menu():
    print("\n-----------------------------------------------------------")
    print("Welcome to HR System!\nPress 1 to Login.\nPress 0 to Exit.")
    print("-----------------------------------------------------------\n")

def menu(userdata):
    empdata = el.load_employee_data()
    employees = e.Employee.parse_from_dictionary(empdata)
    for employee in employees:
        if (userdata.emp_id == employee.emp_id):
            userdata = employee
    print("\nWelcome " + userdata.name + "!")
    if userdata.role_id == 1:
        #1 = employee
        print("-----------------------------------------------------------")
        print("Please kindly choose which option by typing the number.")
        print("1. View My data")
        print("2. Apply Leave")
        print("0. Logout")
        print("-----------------------------------------------------------\n")
    elif userdata.role_id == 2:
        #2 = manager
        print("-----------------------------------------------------------")
        print("Please kindly choose which option by typing the number.")
        print("1. View My Team")
        print("2. Apply Leave")
        print("3. Approve Leave")
        print("0. Logout")
        print("-----------------------------------------------------------\n")
    elif userdata.role_id == 3:
        #3 = admin
        print("-----------------------------------------------------------")
        print("Please kindly choose which option by typing the number.")
        print("1. View All Employee")
        print("2. Apply Leave")
        print("3. Approve Leave")
        print("4. Add Employee")
        print("0. Logout")
        print("-----------------------------------------------------------\n")

def get_option_input():
    opt = raw_input("Input option: ")
    #to check if user input is number or not
    if opt.isdigit():
        return int(opt)
    else:
        return 10 

def login(user,passwd):
    empdata = el.load_employee_data()
    employees = e.Employee.parse_from_dictionary(empdata)
    for employee in employees:
        if employee.email == user:
            if str(employee.password) == passwd:
                print("Login Success!")
                return employee
            else:
                return False

def logout():
    print("Logout success!")

if __name__ == "__main__":
    main()
