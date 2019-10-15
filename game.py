
class Game:
    def __init__(self, id=id, home_score=int, away_score=int, home_team=None, away_team=None):
        self.id = id
        self.home_score = home_score
        self.away_score = away_score
        self.home_team = home_team
        self.away_team = away_team


    def _win(self):
        """Checks for win and add relevant points teams"""
        if self.home_score < self.away_score:
            self.away_team.win()
        elif self.away_score < self.home_score:
            self.home_team.win()


    def _draw(self):
        """Checks for draw and add relevant points to teams"""
        if self.home_score == self.away_score:
            self.away_team.draw()
            self.home_team.draw()


    def _played(self):
        """Adds played game to the team"""
        self.away_team.play_game()
        self.home_team.play_game()

    def _add_goals(self):
        """Checks goals and add points to teams"""
        away_goals = self.away_score
        home_goals = self.home_score

        self.away_team.add_scored_goals(away_goals)
        self.home_team.add_scored_goals(home_goals)

        self.away_team.add_conceded_goals(home_goals)
        self.home_team.add_conceded_goals(away_goals)

    def handle_scores(self):
        """Handles all the scores for one game"""
        self._played()
        self._win()
        self._draw()
        self._add_goals()


    def __str__(self):
        return f'{self.home_team} VS {self.away_team}'