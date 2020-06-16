class Employee:
    def __init__(self, emp_id, name, email, password, role_id, team_id,status_id, leave):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.password = password
        self.role_id = role_id
        self.team_id = team_id
        self.status_id = status_id
        self.leave = leave

    def get_employees_dict(self):
        emp_dict = {"emp_id": self.emp_id,
                    "name": self.name,
                    "email": self.email,
                    "password": self.password,
                    "role_id": self.role_id,
                    "team_id": self.team_id,
                    "status_id": self.status_id,
                    "leave": self.leave}
        return emp_dict
    
    @staticmethod
    def parse_from_dictionary(input):
        employees = input['employees']
        result = []
        for employee in employees:
            parsed = Employee(employee['emp_id'],employee['name'],employee['email'],employee['password'], employee['role_id'],employee['team_id'],employee['status_id'],employee['leave'])
            result.append(parsed)
        return result

    

    
