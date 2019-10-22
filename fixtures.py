from game import Game
from team import Team


class Fixtures():
    def __init__(self, database, tournament_id=None):
        if tournament_id is None:
            self.fixtures = {}
            self.database = database
        else:
            self.database = database
            self.fixtures = self.database.get_fixtures(tournament_id)

    def generate_fixture_list(self, teams: list, total_rounds):
        """Generate fixtures from a list of teams, and returns the fixtures
        as a list"""

        if len(teams) % 2 != 0:
            teams.append(Team(self.database, 0, 'Day Off'))
        n = len(teams)

        match = []
        fixtures_in_rounds = []
        for fixture in range(1, n):
            for i in range(round(n / 2)):
                match.append((teams[i], teams[n - 1 - i]))
            teams.insert(1, teams.pop())
            fixtures_in_rounds.append(match)
            match = []

        fixtures = []

        for rounds in fixtures_in_rounds:
            for game in rounds:
                fixtures.append(game)

        # for fixture in range(1, n):
        #     for i in range(round(n/2)):
        #         return_match.append((teams[n - 1 - i], teams[i]))
        #     teams.insert(1, teams.pop())
        #     fixtures.append(return_match)
        #     return_match = []


        #insert the list into self.fixture dict
        # print(fixtures_in_rounds)
        # print(fixtures * total_rounds, "SINNUM TOTAL ROUNDS")
        # self.insert_fixture_into_dict(fixtures * total_rounds)
        return fixtures * total_rounds


    def insert_fixture_into_dict(self, fixtures: list, tournament_id=None):
        """Inserts fixtures from a list to a dictionary of fixtures were game number
        is the key"""
        # print(fixtures, "jesúskristur á krossinum\n\n")
        # print(len(fixtures), "þetta er len")
        game_nr = 0
        for teams in fixtures:
            home, away = teams[0], teams[1]
            if home.id != 0 or away.id != 0:
                if tournament_id != None:
                    if self.database.is_played(game_id=game_nr, tournament_id=tournament_id):
                        home_score, away_score = self.database.get_scores_for_game(game_id=game_nr)
                        if home_score == 'VIRKAR' or away_score == "EKKI":
                            game_nr+=1
                            continue
                        else:
                            self.fixtures[game_nr] = [teams, [home_score, away_score]]
                            game_nr += 1
                            continue
                else:
                    self.fixtures[game_nr] = [teams, []]
                    game_nr += 1
                    continue

        return self.fixtures

    def insert_score_to_fixture(self, score, gamenr):
        """Inserts a score into the fixture dict with game number as parameter"""
        self.fixtures[gamenr][1].append(score)

    def show_fixtures(self, tournament_id):
        """Shows fixtures when user chooses 2 from menu. If game
            is played it prints the score from the game, else it prints
            not played. Returns nothing."""
        print()
        for game_number, game in self.fixtures.items():
            #game_nr from 0 to number of games

            home, away = game[0] #get teams from list with tuple

            if home.id != 0 or away.id != 0:
                played = self.database.is_played(tournament_id, int(game_number))

                if not played:
                    print("Game:", game_number+1, end=" ")
                    print(home.name, "VS", away.name, end=" ")
                    print("Not played")

                else:
                    #need to implement the else statement
                    print("Game:", game_number+1, end=" ")
                    print(home.name, "VS", away.name, end=" ")
                    if self.fixtures[game_number][1] != []:
                        print("PLAYED, list missing score")
                        # print(self.fixtures[key])
                        # print(self.fixtures[key][1][0][0], " - ",  self.fixtures[key][1][0][1])
                    else:
                        print("PLAYED, list has scores")
                #     print("else lína 70 fixt[key],", self.fixtures[key])
                #         print("else lína 70 fixt[key][1][0],", self.fixtures[key][1])
                    # print(self.fixtures[key][1][0][0], " - ",  self.fixtures[key][1][0][1])


    def __str__(self):
        retval = ""
        for key,value in self.fixtures.items():
            retval += key + " "
            for games in value:
                retval += games
            retval += "\n"
        return retval + "atli"
