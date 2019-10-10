from game import Game

class Fixtures():
    def __init__(self):
        self.fixtures = {}

    def generate_fixture_list(self, teams: list):
        if len(teams) % 2 != 0:
            teams.append('Day off')
        n = len(teams)
        match = []
        fixtures = []

        return_match = []
        for fixture in range(1, n):
            for i in range(round(n/2)):
                match.append((teams[i], teams[n - 1 - i]))
                return_match.append((teams[n - 1 - i], teams[i]))
            teams.insert(1, teams.pop())
            fixtures.append(return_match)
            match = []
            return_match = []

        self._insert_fixture_into_dict(fixtures)
        return fixtures

    def _insert_fixture_into_dict(self, fixtures: list):
        game = 1

        for fixture in fixtures:
            for i in fixture:
                if 'Day off' not in i:
                    self.fixtures[game] = [i, []]
                    game += 1

        for key,value in self.fixtures.items():
            print(key, value)

    def show_fixtures(self):
        for key, value in self.fixtures.items():
            print("Game:",key, end=" ")
            first_team = True
            for the_tuple in value:
                for team in the_tuple:
                    if first_team:
                        print(team, end=" VS ")
                        first_team = False
                    else:
                        print(team)
        print()

    def __str__(self):
        return f''
