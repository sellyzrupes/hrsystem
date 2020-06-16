class Role:
    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name

    def get_role_dict(self):
        role_dict = {"role_id": self.role_id, "role_name": self.role_name}
        return role_dict
    
    @staticmethod
    def parse_from_dictionary(input):
        roles = input
        result = []
        for role in roles:
            parsed = Role(role['role_id'],role['role_name'])
            result.append(parsed)
        return result