import json
import math
import datetime
from Load_Data import employee as el
from Load_Data import load_leave as ll

dataemp = el.load_employee_data()
dataleave = ll.load_leave_data()

def apply_leave(sd,ed,emp_id):
    l = len(dataleave['leaves'])-1
    lastid = int(dataleave['leaves'][l]['leave_id'])+1
    #convert input to epoch
    sdsplit = sd.split("-") 
    asd=[]
    for val in sdsplit:
        asd.append(int(val))
    timestamp1 = datetime.datetime(asd[2], asd[1], asd[0], 0, 0).strftime('%s')
    edsplit = ed.split("-") 
    asd2=[]
    for val2 in edsplit:
        asd2.append(int(val2))
    timestamp2 = datetime.datetime(asd2[2], asd2[1], asd2[0], 0, 0).strftime('%s')
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

#def check_leave(team_id):
