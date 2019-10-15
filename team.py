from mysqldata import DatabaseSearcher

class Team:
    def __init__(self, database, id=None, name=str, points=None, played=None, scored=None, conceded=None):

        #works if team is random from start
        self.id = id
        self.database = database
        self.name = name
        if points:
            self.points = points
        else:
            self.points = 0

        if played:
            self.played_games = played
        else:
            self.played_games = 0

        if scored:
            self.scored_goals = scored
        else:
            self.scored_goals = 0

        if conceded:
            self.conceded_goals = conceded
        else:
            self.conceded_goals = 0

        self.player_dict = {}



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
        return f'{self.name}'
