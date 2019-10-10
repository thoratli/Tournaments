from game import Game

class fixtures():
    def __init__(self):
        self.fixtures = {}



    def generate_fixture_list(self, teams):
        if len(teams) % 2:
            teams.append('Day off')
        n = len(teams)
        match = []
        fixtures = []
        scores = []

        return_match = []
        for fixture in range(1, n):
            for i in range(round(n/2)):
                match.append((teams[i], teams[n - 1 - i]))
                return_match.append((teams[n - 1 - i], teams[i]))
            teams.insert(1, teams.pop())
            fixtures.insert(round(len(fixtures)/2), match)
            fixtures.append(return_match)
            match = []
            return_match = []

        self._insert_fixture_into_dict(fixtures)
        return fixtures.__reversed__()

    def _insert_fixture_into_dict(self, fixtures):
        round = 1
        game = 1

        for fixture in fixtures:
            for i in fixture:
                self.fixtures[game] = [i, []]
                # print(f'Game Number: {game} -- {i}')
                game += 1
                # print()

        for key,value in self.fixtures.items():
            print(key, value)


def main():
    leikir = fixtures()
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    games = leikir.generate_fixture_list(teams)








main()