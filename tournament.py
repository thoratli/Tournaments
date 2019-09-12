from validation import Validation
from player import Player
import random
PADDING = "---------------------------------------------------------"

class Tournament():
    def __init__(self):
        self.validate = Validation()
        self.player = Player()

        self.name = ""
        self.players_list = []
        self.rounds = 0
        self.total_players = 0
        self.total_rounds = 0
        self.fixtures = {}
        self.randomlist = ['Real Madrid', 'Barcelona', 'Liverpool', 'Iceland', 'Brazil',
                           'PSG', '1 star', '2 star', '1 star', '3 star', '4 star','Lowest star',
                           'Everton', 'FifaRandomRule', 'Chelsea', 'Basel', 'Manchester City',
                           'IcelanderTeam', 'Manchester United', 'Arsenal', 'Leicester', 'Ajax',
                           'Atletico Madrid', 'Tottenham', 'Bayern Munchen', 'B. Dortmund', 'Juventus',
                           'Roma', 'Inter Milan']



    def __initial_tournament__(self):
        self.name = self.get_tournament_name()
        self.total_players = self.get_total_players()
        self.total_rounds = self.get_rounds()

        play_random = input("You want to play with random Teams from our list [Y/n]").lower()
        if play_random in 'yY':
            self.get_random_team()
        else:
            self.set_players_name()


    def get_random_team(self):
        players = 0
        # todo implement id system for user
        checklist = []
        for i in range(int(self.total_players)):
            while players == i:
                team = random.choice(self.randomlist)
                if team not in checklist:
                    checklist.append(team)
                    self.player.add_player(team)
                    self.players_list.append(team)
                    players += 1



    def get_tournament_name(self):
        name = input("What is the name of your League: ")
        return name


    def print_league(self):
        #todo: implement values in the print
        #todo: implement size of print so it fits
        print(f'                     {self.name}')
        print("PLAYER            PLAYED   SCORED   CONCEDED   +/-  POINTS")
        print("------            ------   ------   --------   ---  ------")


        for key,value in self.player.player_dict.items():
            if len(value)> 11:
                print(value[0:13] + "...")
                print(PADDING)
            else:
                print(value)
                print(PADDING)


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
                    self.players_list.append(player)
                    players += 1


    def get_rounds(self):
        while True:
            try:
                number = int(input("How many rounds you want to play? "))
                if number > 0:
                    return number
            except:
                print("Please enter a number! ")


    def __total_games_per_round__(self):
        # Added this. Should return the right number of games - Wenni
        return f"{round(((self.total_players*(self.total_players-1))/2))}"


    def create_game(self, team_list):

        game = []
        while len(game) < 2:
            team = random.choice(team_list)
            if team not in game:
                game.append(team)

        return sorted(game)




    def get_fixtures(self):

        #todo: implement the fixtures. Náði ekki að gera það :/

        checklist = []
        counter = 0
        while counter < int(self.__total_games_per_round__()):
            game = self.create_game(self.players_list)

            if game not in checklist:
                checklist.append(game)
                self.fixtures[counter] = game
                counter += 1
        # print(f"You are playing {self.total_rounds} rounds. \n")
        #
        # print(self.fixtures)


    def print_fixtures(self):

        print("    ---- FIXTURES ---")
        for game,teams in self.fixtures.items():
            print(f"Game nr {game+1}: ", end="")
            number_of_teams = 0
            for team in teams:
                if number_of_teams == 0:
                    print(f"{team} ", end="VS ")
                    number_of_teams += 1
                else:
                    print(f"{team}", end=" ")
            print("")

        #todo:implement the names in the value
        #todo:implement pretty print


    def __print_starting_info__(self):
        retval = f'\nSo {self.total_players} players are competing.\n'
        retval += f'You wanted to play {self.total_rounds} rounds.\n'
        retval += f'In total you will play {int(self.__total_games_per_round__())*int(self.total_rounds)} games'
        print(retval)
        return retval


    def __str__(self):
        retval = ""

        for key,value in self.players_list.items():
            retval += f'\nPlayer number {key}: {value.lower().capitalize()}'

        return retval