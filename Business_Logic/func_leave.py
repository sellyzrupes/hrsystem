import json
import math
import datetime
from datetime import timedelta,date
from Load_Data import employee as el
from Load_Data import load_leave as ll
from Models import employee as e
from Models import leave as l

empdata = el.load_employee_data()
employees = e.Employee.parse_from_dictionary(empdata)
leavedata = ll.load_leave_data()
leaves = l.Leave.parse_from_dictionary(leavedata)
peak_periods = l.Leave.get_peak_periods(leavedata)
holidays = l.Leave.get_holidays(leavedata)

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def split_input_date(input):
    datesplit = input.split("-")
    date_temp = [] 
    for val in datesplit:
        date_temp.append(int(val))
    return date_temp

def leave_date_taken(sd,ed):
    sdate = split_input_date(sd)
    start_dt = date(sdate[2], sdate[1], sdate[0])
    edate = split_input_date(ed)
    end_dt = date(edate[2], edate[1], edate[0])
    list_of_leave = []
    for dt in daterange(start_dt, end_dt):
        list_of_leave.append(dt.strftime("%d-%m-%Y"))
    return list_of_leave

def compare_list_date(list_of_leave,peak_periods):
    setperiod = set(peak_periods)
    setlist = set(list_of_leave)
    result = setperiod.intersection(setlist)
    return len(result)

def check_other_member_leave(listleave,userdata):
    members = []
    #get team members, -1 cos manager excluded
    total_member = -1
    for employee in employees:
            if employee.team_id == userdata.team_id:
                members.append(employee.team_id)
                total_member += 1
    #to check emp id on leave data, member whose leave already approved
    save_id = []
    for leave in leaves:
        for employee in employees:
            if (employee.emp_id == leave.emp_id) and (leave.leave_status == 1):
                save_id.append(leave.leave_id)
    counter = 0
    #check if leave between already taken leave
    for leave in leaves:
        memberleave = leave_date_taken(leave.leave_start,leave.leave_end)
        for ids in save_id:
            if (ids == leave.leave_id):
                if(compare_list_date(listleave,memberleave) > 0):
                    counter +=1
    #check final result
    if(counter < total_member):
        return False
    else:
        return True

def update_balance(emp_id,balance):
    temp = []
    for employee in employees:
        if employee.emp_id == int(emp_id):
            employee.leave = employee.leave - balance
        temp.append(employee.get_employees_dict())
    writedata = {
        "employees": temp
    }
    with open('Database/employee.json','w') as emp_file:
        json.dump(writedata, emp_file, indent=4)
            

def apply_leave(start_date,end_date,userdata):
    emp_id = userdata.emp_id
    la = len(leaves)-1
    newid = int(leaves[la].leave_id)+1    
    listleave = leave_date_taken(start_date,end_date)
    pperiod = compare_list_date(listleave,peak_periods)
    #check peak period
    if pperiod > 0:
        print("Cannot take leave during peak period!")
        return None
    if(userdata.role_id!=2):
        pcheck = check_other_member_leave(listleave,userdata)
        if pcheck == True:
            print("Cannot take leave, overlapped with other members!")
            return None
    #to check if leave applied intersect with holiday
    deduct = compare_list_date(listleave,holidays)
    ctr = 0
    #check if leave taken on weekend
    for day in listleave:
        d = split_input_date(day)
        if (date(d[2], d[1], d[0]).weekday() == 5 or date(d[2], d[1], d[0]).weekday() == 6):
            ctr +=1
    final_balance = len(listleave) - deduct - ctr
    status = 0
    if(userdata.role_id == 2):
        status = 1
    newdata = l.Leave(newid,emp_id,status,start_date,end_date,final_balance)
    leaves.append(newdata)
    #change model to dict
    temp = []
    for leave in leaves:
        temp.append(leave.get_leave_dict())
    writedata = {
        "leaves": temp,
        "peak_periods": peak_periods,
        "holidays":holidays
    }
    with open('Database/leave.json','w') as emp_file:
        json.dump(writedata, emp_file, indent=4)
    print("Added Successfully!")
    update_balance(emp_id,final_balance)

def print_leave(leave,userdata):
    print("\n-----------------------------------------------------------")
    print("Employee ID : " + str(leave.emp_id))
    print("Start : " + leave.leave_start)
    print("End : " + leave.leave_end)
    print("Total Leave Deducted : " + str(leave.leave_balance))
    print("-----------------------------------------------------------\n")

def view_pending_leave(userdata):
    members = []
    #to get team members employee id
    for employee in employees:
            if employee.team_id == userdata.team_id:
                members.append(employee.emp_id)
    #to check emp id on leave data
    counter = 0
    for leave in leaves:
        for member in members:
            if (member == leave.emp_id) and (leave.leave_status == 0):
                print_leave(leave,userdata)
                counter +=1
    if(counter == 0):
        print ("No leave to be approved")

def approve_leave(emp_id, stat):
    temp = []
    for leave in leaves:
        if leave.emp_id == int(emp_id):
            leave.leave_status = stat
        temp.append(leave.get_leave_dict())
    writedata = {
        "leaves": temp,
        "peak_periods": peak_periods,
        "holidays":holidays
    }
    with open('Database/leave.json','w') as emp_file:
        json.dump(writedata, emp_file, indent=4)
    if stat == 2:
        print("Leave Rejected! Leave Balance will be returned to the owner")
        #add deduct balance
    elif stat == 1:
        print("Leave Approved!")