from validation import Validation
from player import Player

class Tournament():
    def __init__(self):
        self.validate = Validation()
        self.player = Player()

        self.name = ""
        self.players_list = {}
        self.rounds = 0
        self.total_players = 0
        self.total_rounds = 0
        self.fixtures = {}



    def __initial_tournament__(self):
        self.name = self.get_tournament_name()
        self.total_players = self.get_total_players()
        self.total_rounds = self.get_rounds()
        self.set_players_name()
        # self.fixtures = self.get_fixtures()



    def get_tournament_name(self):
        name = input("What is the name of your League: ")
        return name


    def print_league(self):
        #todo: implement values in the print
        #todo: implement size of print so it fits

        print(f'\n                  ---- {self.name} ----')
        print("PLAYER       PLAYED     SCORED    CONCEDED    +/-    POINTS")

        for key,value in self.player.player_dict.items():
            print(key, value)


    def get_total_players(self):

        while True:
            players = input("How many players: ")
            if self.validate.validate_integer(players):
                return int(players)


    def set_players_name(self):

        players = 0
        #todo implement id system for user

        for i in range(int(self.total_players)):
            while players == i:
                player = input(f'Participant nr {players +1}: ')
                if self.validate.validate_name_input(player):
                    self.player.add_player(player)
                    self.players_list[i+1] = player
                    players += 1


    def get_rounds(self):
        while True:
            try:
                number = int(input("How many rounds you want to play? "))
                if number > 0:
                    return number
            except:
                print("Please enter a number! ")


    def __total_games__(self):
        # Added this. Should return the right number of games - Wenni
        return f"{round((((self.total_players*(self.total_players-1))/2)* self.total_rounds))}"


    def get_fixtures(self):

        #todo: implement the fixtures. Náði ekki að gera það :/

        # deiling = len(self.players_list)
        # for nr in range(1, int(self.__total_games__()+1), (self.total_players)-1):
        #
        #     self.fixtures[nr] = [self.players_list[nr], self.players_list[nr+1]]
        #     self.fixtures[nr+1] = [self.players_list[nr+2], self.players_list[nr+3]]



        return self.fixtures


    def print_fixtures(self):

        print("    ---- FIXTURES ---")
        for game,teams in self.fixtures.items():

            print(f"Game nr {game}: ", end = "")
            for team in teams:
                print(f"{team} ",end = " ")
            print("")

        #todo:implement the names in the value
        #todo:implement pretty print


    def __print_starting_info__(self):
        retval = f'\nSo {self.total_players} players are competing.\n'
        retval += f'You wanted to play {self.total_rounds} rounds.\n'
        retval += f'In total you will play {self.__total_games__()} games\n'
        print(retval)
        return retval


    def __str__(self):
        retval = ""

        for key,value in self.players_list.items():
            retval += f'\nPlayer number {key}: {value.lower().capitalize()}'

        return retval