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
        self.games = self.mot.__total_games__()
        self.players_dict = self.mot.players_list
        print(self.mot.__print_starting_info__())
        self.fixtures = {}
        self.fixtures = self.mot.get_fixtures()
        self.print_fixtures()


    def print_league(self):
        self.mot.print_league()


    def start_tournament(self):
        game_on = 0

        while game_on < int(self.games):

            #todo: implement the tournament games
            print(f'PLAYING GAME NR: {game_on+1}')
            print(self.fixtures[game_on+1])
            home_score, away_score = self.validation.validate_score_input()
            self.fixtures[game_on+1][1] = (home_score, away_score)
            # if homescore and awayscore:
            game_on += 1

        # print(self.fixtures)
        #todo: implement how to keep score


    def print_fixtures(self):
        pass
        # for key,value in self.fixtures.items():
        #     print(f'Game nr:{key}, Teams: {value}')

        #implement the names in the value
        #implement pretty print


    def get_scores_from_input(self):
        #todo: get input from user, the score of a game and store it somehow
        try:
            score = input("Enter the scores with space between, 2 2: ").split()
            print(score, "yesyeyss")
            if len(score) == 2:
                print("YES")
                homescore, awayscore = self.validation.validate_score_input(score)
                return int(homescore), int(awayscore)
            else:
                return False, False
        except:
            print("Please try again, bitch!")
            return False, False


    def show_league_table(self):
        # todo: implement a function which shows the league table at any given time
        pass