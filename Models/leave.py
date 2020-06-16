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
            "emp_id": self.emp_id,
            "leave_status": self.leave_status,
            "leave_start": self.leave_start,
            "leave_end": self.leave_end,
            "leave_balance": self.leave_balance
            }
        return leave_dict

    @staticmethod
    def parse_from_dictionary(input):
        leaves = input['leaves']
        result = []
        for leave in leaves:
            parsed = Leave(leave['leave_id'],leave['emp_id'],leave['leave_status'],leave['leave_start'],leave['leave_end'],leave['leave_balance'])
            result.append(parsed)
        return result

    @staticmethod
    def get_peak_periods(input):
        peak_periods = input['peak_periods']
        result = []
        for peak_period in peak_periods:
            result.append(peak_period)
        return result
    
    @staticmethod
    def get_holidays(input):
        holidays = input['holidays']
        result = []
        for holiday in holidays:
            result.append(holiday)
        return result