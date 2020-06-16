class Team:
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name

    def get_team_dict(self):
        team_dict = {"team_id": self.team_id, "team_name": self.team_name}
        return team_dict

    @staticmethod
    def parse_from_dictionary(input):
        teams = input
        result = []
        for team in teams:
            parsed = Team(team['team_id'],team['team_name'])
            result.append(parsed)
        return result