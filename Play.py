from Tournaments import Tournament

class Play:

    def __init__(self):
        mot = Tournament()
        self.number_of_players = mot.total_players
        self.rounds = mot.rounds
        self.games = mot.__total_games__()
        self.players_dict = mot.players_list
        print(mot.__print_starting_info__())
        self.game_on = 0
        # self.tuples = mot.create_pair_of_tubles()
        self.fixtures = mot.fixtures
        self.print_fixtures()


    def start_tournament(self):
        while self.game_on < int(self.games):
            print(f'Leikur {self.game_on + 1} í gangi')
            self.game_on += 1


    def print_fixtures(self):
        for key,value in self.fixtures.items():
            print(f'Game nr: {key}, Teams: {value}')
            #implement the names in the value

    def get_scores_from_input(self):
        #Todo: get input from user, the score of a game and store it somehow
        pass


    def show_league_table(self):
        # todo: implent a function which shows the league table at any given time
        pass