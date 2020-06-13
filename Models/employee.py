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
