import json
import math
import datetime
from Load_Data import employee as el
from Load_Data import load_leave as ll

dataemp = el.load_employee_data()
dataleave = ll.load_leave_data()

def check_peak_period(sd,ed):
    counter = False
    for val in dataleave['peak_periods']:
        if (sd <= val) and (ed >= val):
            counter = True
    return counter

def check_other_member_leave(sd,ed,userdata):
    save_emp = []
    #get team members
    total_member = -1
    for emp in dataemp['employees']:
            if emp['team_id'] == userdata['team_id']:
                save_emp.append(emp['emp_id'])
                total_member += 1
    #print(total_member)
    #to check emp id on leave data
    save_id = []
    for teamleave in dataleave['leaves']:
        for test in save_emp:
            if (test == teamleave['emp_id']) and (teamleave['leave_status'] == 1):
                save_id.append(teamleave['leave_id'])
    #print(save_id)
    counter = 0
    #check if leave between already taken leave
    for teamleave in dataleave['leaves']:
        for member in save_id:
            if (member == teamleave['leave_id']):
                #print("masuk")
                if (teamleave['leave_start']<= sd and teamleave['leave_end'] >= sd):
                    counter +=1
                if (teamleave['leave_start']<= ed and teamleave['leave_end'] >= ed):
                    counter +=1
                if (math.fabs(sd-teamleave['leave_start']) <= 86400) or (math.fabs(ed-teamleave['leave_end']) <= 86400):
                    counter +=1
    #print(counter)
    #check final result
    if(counter < (total_member-1)*2):
        return False
    else:
        return True



    

#def add_leave(stime,etime,emp_id,status):
#    l = len(dataleave['leaves'])-1
#    leave_id = int(dataleave['leaves'][l]['leave_id'])+1
#    selisih = int(math.floor((int(etime) - int(stime))/86400))

def validation_check_leave(sd,ed):
    days_of_leave = int(math.ceil((ed - sd)/86400))
    #print(days_of_leave)
    counter = 0
    for val in dataleave['holidays']:
        if sd <= val and ed >= val:
            counter +=1
        if (math.fabs(sd-val) <= 86400) or (math.fabs(ed-val) <= 86400):
            counter +=1
    #print("holiday counter: " + str(counter))
    #sdate =
    #edate
    datecount = sd 
    for i in range(days_of_leave):
        #print i
        if (int(datetime.datetime.fromtimestamp(datecount).weekday()) == 5 or int(datetime.datetime.fromtimestamp(datecount).weekday()) == 6):
            counter +=1
            #print(counter)
        datecount += 86400
    finalresult = days_of_leave - counter + 1
    return finalresult

    #checkisholiday
#    counter = 0
#    for asd in selisih:
#        if check holiday
#        elif weekend po bukan

#def write_leave()
#
def apply_leave(sd,ed,userdata):
    emp_id = userdata['emp_id']
    l = len(dataleave['leaves'])-1
    lastid = int(dataleave['leaves'][l]['leave_id'])+1
    starttime = date_to_epoch(sd)
    endtime = date_to_epoch(ed)
    pperiod = check_peak_period(starttime,endtime)
    #check peak period
    if pperiod == True:
        print("Cannot take leave during peak period!")
        return None
    #if not manager, need to check overlapped members
    if(userdata['role_id']!=2):
        pcheck = check_other_member_leave(starttime,endtime,userdata)
        if pcheck == True:
            print("Cannot take leave, overlapped with other members!")
            return None
    balance = validation_check_leave(starttime,endtime)
    inputleave = {
        "leave_id": lastid,
        "emp_id": emp_id, 
        "leave_status": 0,
        "leave_start": starttime,
        "leave_end": endtime,
        "leave_balance": balance
    }
    dataleave['leaves'].append(inputleave)
    with open('Database/leave.json','w') as emp2:
        json.dump(dataleave, emp2, indent=4)
    #check holiday and workday

    

    
    #print(pcheck)
    days_of_leave = int(math.floor((int(endtime) - int(starttime))/86400))

    
    #if userdata['role_id']==2:



    
    #emp_id = userdata['emp_id']
    #l = len(dataleave['leaves'])-1
    #lastid = int(dataleave['leaves'][l]['leave_id'])+1
    #convert input to epoch
    #sdsplit = sd.split("-") 
    #asd=[]
    #for val in sdsplit:
    #    asd.append(int(val))
    #timestamp1 = datetime.datetime(asd[2], asd[1], asd[0], 0, 0).strftime('%s')
    #timestamp1 = date_to_epoch(sd)
    #edsplit = ed.split("-") 
    #asd2=[]
    #for val2 in edsplit:
    #    asd2.append(int(val2))
    #timestamp2 = datetime.datetime(asd2[2], asd2[1], asd2[0], 0, 0).strftime('%s')
    #timestamp2 = date_to_epoch(ed)
    #selisih = int(math.floor((int(timestamp2) - int(timestamp1))/86400))
    #inputleave = {
    #    "leave_id": lastid,
    #    "emp_id": emp_id, 
    #    "leave_status": 0,
    #    "leave_start": timestamp1,
    #    "leave_end": timestamp2,
    #    "leave_balance": selisih
    #}
    #dataleave['leaves'].append(inputleave)
    #with open('Database/leave.json','w') as emp2:
    #    json.dump(dataleave, emp2, indent=4)

def epoch_to_date(epochtime):
    date = datetime.date.fromtimestamp(epochtime).strftime("%d-%m-%Y")
    return date

def date_to_epoch(date):
    datesplit = date.split("-") 
    date_temp=[]
    for val in datesplit:
        date_temp.append(int(val))
    timestamp = int(datetime.datetime(date_temp[2], date_temp[1], date_temp[0], 0, 0).strftime('%s'))
    return timestamp




def print_leave(teamleave,userdata):
    print("\n-----------------------------------------------------------")
    print("Employee ID : " + str(teamleave['emp_id']))
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
        #add deduct balance
    elif stat == 1:
        print("Leave Approved!")


    
