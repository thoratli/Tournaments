

class Team:
    def __init__(self, name=str):
        self.id = 0
        self.player_dict = {}
        self.name = name
        self.points = 0
        self.played_games = 0
        self.scored_goals = 0
        self.conceded_goals = 0


    def get_name(self):
        return self.name

    def add_points(self):

        self.points += 3

    def scored_goals(self):
        return self.scored_goals

    def conceded_goals(self):
        return self.conceded_goals

    def add_team(self, name):
        self.player_dict[self.id] = name
        self.id += 1



    def __str__(self):
        #þetta prentar fixtures
        return f'{self.name}'
