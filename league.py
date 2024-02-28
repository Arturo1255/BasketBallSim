class League:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams

    def addTeam(self, team):
        self.teams.append(team)

    def getName(self):
        return self.name

    def getTeams(self):
        return self.teams
