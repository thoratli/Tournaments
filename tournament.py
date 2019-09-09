from validation import Validation
from player import Player
# from options import Options

class Tournament():
    def __init__(self):
        self.validate = Validation()
        # self.options = Options()
        self.player = Player()

        self.name = ""
        self.players_list = {}
        self.rounds = 0
        self.total_players = 0
        self.total_rounds = 0
        self.__get_players_name__()

    # def __create_tournament__(self):

    def __initial_tournament__(self):
        self.name = self.__get_tournament_name()
        self.total_players = self.__get_total_players__()
        self.total_rounds = self.__get_rounds__()


    def __get_tournament_name(self):
        name = input("What is the name of your League: ")
        return name

    def print_league(self):
        #todo: implement values in the print
        #todo: implement size of print so it fits

        print(f'\n                  ---- {self.name} ----')
        print("PLAYER       PLAYED     SCORED    CONCEDED    +/-    POINTS")

        for key,value in self.player.player_dict.items():
            print(self.player)



    def __get_total_players__(self):

        while True:
            players = input("How many players: ")
            if self.validate.validate_integer(players):
                return int(players)


    def __get_players_name__(self):

        players = 0
        #todo implement id system for user

        for i in range(int(self.total_players)):
            while players == i:
                player = input(f'Participant nr {players +1}: ')
                if self.validate.validate_name_input(player):
                    self.player.add_player(player)
                    self.players_list[i+1] = player
                    players += 1



    def __get_rounds__(self):
        while True:
            try:
                number = int(input("How many rounds you want to play? "))
                if number > 0:
                    return number
            except:
                print("Please enter a number! ")


    def __total_games__(self):
        return f'{(round(self.total_players/2)*(self.total_players-1))}'


    def get_fixtures(self):

        fixtures = {}
        for i in range(1, int(self.__total_games__())+1):
            fixtures[i] = []
            fixtures[i].append([i, i+1])
            fixtures[i].append(['EMPTY FOR SCORES'])

            #todo: implement algorithm so everybody plays with everybody

        return fixtures



    def __print_starting_info__(self):
        retval = f'\nSo {self.total_players} players are competing.\n'
        retval += f'You wanted to play {self.total_rounds} rounds.\n'
        retval += f'In total you will play {self.__total_games__()} games\n'
        return retval


    def __str__(self):
        retval = ""

        for key,value in self.players_list.items():
            retval += f'\nPlayer number {key}: {value.lower().capitalize()}'

        return retval