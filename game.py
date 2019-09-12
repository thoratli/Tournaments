class Game():
    def __init__(self, home_score=int, away_score=int, home_team=str, away_team=str):

        self.home_score = home_score
        self.away_score = away_score
        self.home_team = home_team
        self.away_team = away_team

    def handle_scores(self):

        if self.away_score > self.home_score:
            pass



    def __str__(self):
        return f'{self.home_team} VS {self.away_team}'