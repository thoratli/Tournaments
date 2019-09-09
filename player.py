

class Player:
    def __init__(self, name= str, ):
        self.id = 0
        self.player_dict = {}
        self.name = name
        self.points = 0
        self.played_games = 0
        self.scored_goals = 0
        self.conceded_goals = 0


    def get_name(self):
        return self.name

    def get_poins(self):
        return self.points

    def scored_goals(self):
        return self.scored_goals

    def conceded_goals(self):
        return self.conceded_goals

    def add_player(self, name):
        self.player_dict[self.id] = name
        self.id += 1



    def __str__(self):
        return f'{self.name()} <--- {self.played_games} ---{self.scored_goals}' \
            f' --- {self.conceded_goals} --- {int(self.scored_goals)-int(self.conceded_goals)} --- {self.points}'
