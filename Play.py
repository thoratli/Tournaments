from Tournaments import Tournament

TEAMS = ['Real Madrid', 'Barcelona', 'Liverpool', 'PSG', 'Brazil', 'Iceland', 'Pick 2starred team',
         'Italy', 'Belgium', 'Pick a 3starred team', 'Fifa Random Rule', 'Your competitor picks for you',
         'Scandinavia', 'Spain', 'Netherland', 'Pick 2 star lower than your opponent']

class Play:

    def __init__(self):
        mot = Tournament()
        self.number_of_players = mot.total_players
        self.rounds = mot.rounds
        self.games = mot.__total_games__()
        self.players_dict = mot.players_list
        print(mot.__print_starting_info__())
        self.fixtures = {}
        self.fixtures = mot.get_fixtures()
        self.print_fixtures()


    def start_tournament(self):
        game_on = 0

        while game_on < int(self.games):
            game_on += 1

            print(f'PLAYING GAME NR: {game_on}')
            print(self.fixtures[game_on])
            score = self.get_scores_from_input()
            self.fixtures[game_on][1] = score

        print(self.fixtures
              )
        #todo: implement how to keep score


    def print_fixtures(self):
        pass
        # for key,value in self.fixtures.items():
        #     print(f'Game nr:{key}, Teams: {value}')

            #implement the names in the value
            #implement pretty print


    def get_scores_from_input(self):
        #Todo: get input from user, the score of a game and store it somehow
        while True:
            try:
                score = input("Enter the scores with space between, 2 2: ").split()
                if len(score) == 2:
                    return score
                else:
                    print("Please try again, bitch!")
            except:
                print("Please try again, and be careful.")


    def show_league_table(self):
        # todo: implent a function which shows the league table at any given time
        pass