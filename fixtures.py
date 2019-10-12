from game import Game
from team import Team
from mysqldata import DatabaseSearcher

class Fixtures():
    def __init__(self, database, id=None):
        if id is None:
            self.fixtures = {}
            self.database = database
        else:
            self.database = DatabaseSearcher()
            self.fixtures = self.database.get_fixtures(id)

    def generate_fixture_list(self, teams: list):
        """Generate fixtures from a list of teams, and returns the fixtures
        as a list"""

        if len(teams) % 2 != 0:
            teams.append(Team('Day Off'))
        n = len(teams)
        fixtures = []
        return_match = []

        for fixture in range(1, n):
            for i in range(round(n/2)):
                return_match.append((teams[n - 1 - i], teams[i]))
            teams.insert(1, teams.pop())
            fixtures.append(return_match)
            return_match = []

        #insert the list into self.fixture dict
        self.insert_fixture_into_dict(fixtures)
        return fixtures

    def insert_fixture_into_dict(self, fixtures: list):
        """Inserts fixtures from a list to a dictionary of fixtures were game number
        is the key"""
        game = 1
        for fixture in fixtures:
            for i in fixture:
                #zero represents not played
                self.fixtures[game] = [i, 0]
                game += 1
        return self.fixtures

    def show_fixtures(self, tournament_id):
        """Shows fixtures when user chooses 2 from menu. If game
        is played it prints the score from the game, else it prints
        not played. Returns nothing."""

        games = 1
        i = 0

        for key, value in self.fixtures.items():
            #key from 1 to number of games
            i += 1
            game = value[0]
            home, away = game #get values from tuple
            played = self.database.is_played(tournament_id, str(key))

            if home.name != 'Day Off' and away.name != 'Day Off':
                if not played:
                    print("Game:", games, end=" ")
                    print(home, "VS", away, end=" ")
                    games += 1
                    print("NOT played")

                else:
                    print("What to do here? ")
        print()

    def __str__(self):
        retval = ""
        for key,value in self.fixtures.items():
            retval += key + " "
            for games in value:
                retval += games
            retval += "\n"
        return retval + "atli"
