from game import Game
from team import Team
from mysqldata import DatabaseSearcher

class Fixtures():
    def __init__(self, id=None):
        if id is None:
            self.fixtures = {}
        else:
            database = DatabaseSearcher()
            self.fixtures = database.get_fixtures(id)

    def generate_fixture_list(self, teams: list):
        if len(teams) % 2 != 0:
            teams.append(Team('Day Off'))
        n = len(teams)
        # match = []
        fixtures = []

        return_match = []
        for fixture in range(1, n):
            for i in range(round(n/2)):
                return_match.append((teams[n - 1 - i], teams[i]))
            teams.insert(1, teams.pop())
            fixtures.append(return_match)
            return_match = []

        self.insert_fixture_into_dict(fixtures)
        return fixtures

    def insert_fixture_into_dict(self, fixtures: list):
        game = 1

        for fixture in fixtures:
            for i in fixture:
                #zero represents not played
                self.fixtures[game] = [i, 0]
                game += 1
        return self.fixtures

        # for key,value in self.fixtures.items():
        #     print(key, value)

    def show_fixtures(self):
        i = 1
        for key, value in self.fixtures.items():
            game = value[0]
            home, away = game
            played = value[1]
            if 'Day Off' in game:
                print("dayoff er í game!!! -----------")
            if home != 'Day Off' and away != 'Day Off':
                print("Game:", i, end=" ")
                print(home, "VS", away, end=" ")
                i += 1
            if played == 1:
                print("ALREADY PLAYED, SCORES: 2 2")
            else:
                print("Not played")
        print()



    def __str__(self):
        retval = ""
        for key,value in self.fixtures.items():
            retval += key + " "
            for games in value:
                retval += games
            retval += "\n"
        return retval + "atli"
