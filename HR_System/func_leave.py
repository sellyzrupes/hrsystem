import json
import math
import datetime
from Load_Data import employee as el
from Load_Data import load_leave as ll

dataemp = el.load_employee_data()
dataleave = ll.load_leave_data()

def apply_validation_leave(userdata):
    print("test")

def apply_leave(sd,ed,userdata):
    #if(userdata['role_id'])
    emp_id = userdata['emp_id']
    l = len(dataleave['leaves'])-1
    lastid = int(dataleave['leaves'][l]['leave_id'])+1
    #convert input to epoch
    #sdsplit = sd.split("-") 
    #asd=[]
    #for val in sdsplit:
    #    asd.append(int(val))
    #timestamp1 = datetime.datetime(asd[2], asd[1], asd[0], 0, 0).strftime('%s')
    timestamp1 = date_to_epoch(sd)
    #edsplit = ed.split("-") 
    #asd2=[]
    #for val2 in edsplit:
    #    asd2.append(int(val2))
    #timestamp2 = datetime.datetime(asd2[2], asd2[1], asd2[0], 0, 0).strftime('%s')
    timestamp2 = date_to_epoch(ed)
    selisih = int(math.floor((int(timestamp2) - int(timestamp1))/86400))
    inputleave = {
        "leave_id": lastid,
        "emp_id": emp_id, 
        "leave_status": 0,
        "leave_start": timestamp1,
        "leave_end": timestamp2,
        "leave_balance": selisih
    }
    dataleave['leaves'].append(inputleave)
    with open('Database/leave.json','w') as emp2:
        json.dump(dataleave, emp2, indent=4)

def epoch_to_date(epochtime):
    date = datetime.date.fromtimestamp(epochtime).strftime("%d-%m-%Y")
    return date

def date_to_epoch(date):
    datesplit = date.split("-") 
    date_temp=[]
    for val in datesplit:
        date_temp.append(int(val))
    timestamp = datetime.datetime(date_temp[2], date_temp[1], date_temp[0], 0, 0).strftime('%s')
    return timestamp

#def check_peak_period(sd,ed):

def print_leave(teamleave,userdata):
    print("\n-----------------------------------------------------------")
    print("Employee ID : " + str(teamleave['emp_id']))
    print("Name : " + userdata['name'])
    startdate = epoch_to_date(teamleave['leave_start'])
    print("Start : " + startdate)
    enddate = epoch_to_date(teamleave['leave_end'])
    print("End : " + enddate)
    print("Total Leave Deducted : " + str(teamleave['leave_balance']))
    print("-----------------------------------------------------------\n")


def view_pending_leave(userdata):
    save_emp = []
    #to get team members employee id
    for emp in dataemp['employees']:
            if emp['team_id'] == userdata['team_id']:
                save_emp.append(emp['emp_id'])
    #to check emp id on leave data
    counter = 0
    for teamleave in dataleave['leaves']:
        for test in save_emp:
            if (test == teamleave['emp_id']) and (teamleave['leave_status'] == 0):
                print_leave(teamleave,userdata)
                counter +=1
    if(counter == 0):
        print ("No leave to be approved")

def approve_leave(emp_id, stat):
    for teamleave in dataleave['leaves']:
        if teamleave['emp_id'] == int(emp_id):
            teamleave['leave_status'] = stat
    with open('Database/leave.json','w') as emp2:
        json.dump(dataleave, emp2, indent=4)
    if stat == 2:
        print("Leave Rejected! Leave Balance will be returned to the owner")
    elif stat == 1:
        print("Leave Approved!")


    
