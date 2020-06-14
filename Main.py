#from hr.position import load_positions
#from hr.title import load_titles
#from hr.status import load_status
#from hr.leave_status import load_leave
#from hr.product_line import load_product_lines
#from hr.feature import load_features
#from hr.input_validation import get_option_input
#from hr.employee_manager import employee_manager as em
#from hr.input_validation import get_modify_input, get_delete_input, \
#    get_record_input, get_record_score
#from hr_functions.find_qa_feature import find_qa_feature
#from hr_functions.search_qa import search_emp
#from hr_functions.list_qa_support import list_feature_team
#from hr_functions.display_qa import display_info
#from hr_functions.show_qa import show_emp
import config_variables as cv
from Load_Data import employee as el
from Models import employee as e
from HR_System import view_employee as ve

def main():
    #TODO: write the function to run the different options. Handle the case for various user_roles.
    login_option = True
    while login_option == True:
        login_menu()
        login_option = get_option_input()
        user = raw_input("Input username/email: ")
        passwd = raw_input("Input password: ")
        userdata = login(user,passwd)
        if bool(userdata) == True:
            menu_option = True
            while menu_option == True:
                menu(userdata)
                menu_option = get_option_input()
                if(menu_option == 0):
                    logout()
                    print("Logout success!")
                elif (menu_option == 1):
                    ve.view_emp(userdata)
        else:
            print("Wrong input, please try again")
    print("The program will quit now.")
    #while login_option:
    #    if option == 1:
    #        user = raw_input("Input username/email: ")
    #        passwd = raw_input("Input password: ")
    #        userdata = login(user,passwd)
    #        menu()
    #    elif option == 0:
    #        print("The program will quit now.")
    #        return False

def login_menu():
    print("\n-----------------------------------------------------------")
    print("Welcome to HR System!\nPress 1 to Login.\nPress 0 to exit.")
    print("-----------------------------------------------------------\n")


def menu(userdata):
    if userdata['role_id'] == 1:
        #1 = employee
        print("\n-----------------------------------------------------------")
        print("Please kindly choose which option by typing the number.")
        print("1. View My data")
        print("2. Apply Leave")
        print("0. Exit")
        print("-----------------------------------------------------------\n")
    elif userdata['role_id'] == 2:
        #2 = manager
        print("\n-----------------------------------------------------------")
        print("Please kindly choose which option by typing the number.")
        print("1. View My Team")
        print("2. Apply Leave")
        print("3. Approve Leave")
        print("0. Exit")
        print("-----------------------------------------------------------\n")
    elif userdata['role_id'] == 3:
        #3 = admin
        print("\n-----------------------------------------------------------")
        print("Please kindly choose which option by typing the number.")
        print("1. View All Employee")
        print("2. Apply Leave")
        print("3. Approve Leave")
        print("4. Add Employee")
        print("0. Exit")
        print("-----------------------------------------------------------\n")

def get_option_input():
    opt = raw_input("Input option: ")
    return int(opt)

def login(user,passwd):
    dataemp = el.load_employee_data()
    #print(dataemp['employees'])
    for val in dataemp['employees']:
        if val['email'] == user:
            if str(val['password']) == passwd:
                print("Login Success!")
                return val
            else:
                return False   
    #yuhu = e.Employee(coba['employees']['emp_id'],coba['employees']['name'],coba['employees']['email'],coba['employees']['password'],coba['employees']['role_id'],coba['employees']['team_id'],coba['employees']['status_id'],coba['employees']['leave'])
    #Employee()

def logout():
    ctr = 0
    return ctr

if __name__ == "__main__":
    main()
