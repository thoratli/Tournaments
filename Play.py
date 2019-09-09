from tournament import Tournament
from validation import Validation

TEAMS = ['Real Madrid', 'Barcelona', 'Liverpool', 'PSG', 'Brazil', 'Iceland', 'Pick 2starred team',
         'Italy', 'Belgium', 'Pick a 3starred team', 'Fifa Random Rule', 'Your competitor picks for you',
         'Scandinavia', 'Spain', 'Netherland', 'Pick 2 star lower than your opponent']

class Play:
    def __init__(self):
        self.validation = Validation()
        self.mot = Tournament()
        self.number_of_players = self.mot.total_players
        self.rounds = self.mot.rounds
        self.games = self.mot.total_games()
        self.players_dict = self.mot.players_list
        print(self.mot.__print_starting_info__())
        self.game = 0



    def play_next_game(self, total_games):
        # todo: implement the tournament games

        self.game += 1
        print(self.players_dict
              )
        print(f'Game number: {self.game}')

        # while True:
        #     scores = self.get_scores_from_input()
        #     if self.validation.validate_score_input(scores):
        #         home, away = self.convert_score_string_to_numbers(scores)
        #         break



        # print(self.fixtures[game_on+1])
        #
        # home_score, away_score = self.validation.validate_score_input()
        # self.fixtures[game_on+1][1] = (home_score, away_score)
        # # if homescore and awayscore:

        # print(self.fixtures)
        #todo: implement how to keep score


    def get_scores_from_input(self):
        #todo: get input from user, the score of a game and store it somehow
            score = input("Enter the scores with space between, 2 2: ")
            return score

    def convert_score_string_to_numbers(self, score):
        home, away = score.split()
        return int(home), int(away)
