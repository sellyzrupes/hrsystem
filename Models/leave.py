class Leave:
    def __init__(self, leave_id, emp_id, leave_status, leave_start, leave_end, leave_balance):
        self.leave_id = leave_id
        self.emp_id = emp_id
        self.leave_status = leave_status
        self.leave_start = leave_start
        self.leave_end = leave_end
        self.leave_balance = leave_balance

    def get_leave_dict(self):
        leave_dict = {
            "leave_id": self.leave_id,
            "emp_id": self.emp_id 
            "leave_status": self.leave_status,
            "leave_start": self.leave_start,
            "leave_end": self.leave_end,
            "leave_balance": self.leave_balance
            }
        return leave_dict
