

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

    def win(self):
        self.points += 3

    def draw(self):
        self.points += 1

    def add_scored_goals(self, goals):
        self.scored_goals += int(goals)

    def add_conceded_goals(self,goals):
        self.conceded_goals += int(goals)

    def add_team(self, name):
        self.player_dict[self.id] = name
        self.id += 1

    def play_game(self):
        self.played_games += 1


    def __str__(self):
        #þetta prentar fixtures
        return f'{self.name}'
