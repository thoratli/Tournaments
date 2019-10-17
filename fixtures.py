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
        fixtures = []
        return_match = []

        for fixture in range(1, n):
            for i in range(round(n/2)):
                return_match.append((teams[n - 1 - i], teams[i]))
            teams.insert(1, teams.pop())
            fixtures.append(return_match)
            return_match = []

        #insert the list into self.fixture dict
        self.insert_fixture_into_dict(fixtures * total_rounds)
        return fixtures * total_rounds


    def insert_fixture_into_dict(self, fixtures: list, tournament_id=None):
        """Inserts fixtures from a list to a dictionary of fixtures were game number
        is the key"""
        game_nr = 0
        for fixture in fixtures:
            for teams in fixture:
                    if teams[0].id != 0 and teams[1].id != 0:
                        # if new game, all scores are empty
                        if tournament_id != None:
                            if self.database.is_played(game_id=game_nr, tournament_id=tournament_id):
                                home_score, away_score = self.database.get_scores_for_game(game_id=game_nr)
                                if home_score == 'VIRKAR' or away_score == "EKKI":
                                    game_nr+=1
                                    break
                                else:
                                    self.fixtures[game_nr] = [teams, [home_score, away_score]]
                                    game_nr += 1
                                    break
                        else:
                            self.fixtures[game_nr] = [teams, []]
                            game_nr += 1
                            break

        return self.fixtures

    def insert_score_to_fixture(self, score, gamenr):
        """Inserts a score into the fixture dict with game number as parameter"""
        self.fixtures[gamenr][1].append(score)

    def show_fixtures(self, tournament_id):
        """Shows fixtures when user chooses 2 from menu. If game
            is played it prints the score from the game, else it prints
            not played. Returns nothing."""
        print()
        for key, value in self.fixtures.items():
            #key from 0 to number of games

            game = value[0]
            home, away = game #get values from tuple
            played = self.database.is_played(tournament_id, int(key))

            if not played:
                print("Game:", key+1, end=" ")
                print(home, "VS", away, end=" ")
                print("Not played")

            else:
                #need to implement the else statement
                print("Game:", key+1, end=" ")
                print(home, "VS", away, end=" ")
                if self.fixtures[key][1] != []:
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
