from validation import Validation
from team import Team
import random
import operator
PADDING = "--------------------------------------------------------------"
MIDDLE = int(len(PADDING)/2)

class Tournament():
    def __init__(self):
        self.validate = Validation()
        self.player = Team()
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


    def get_tournament_name(self):
        name = input("What is the name of your League: ")
        return name



    def set_players_name(self):

        players = 0
        #todo implement id system for user

        for i in range(int(self.total_players)):
            while players == i:
                team_name = input(f'Participant nr {players +1}: ')
                if self.validate.validate_name_input(team_name):
                    new_team = Team(team_name)
                    self.players_list.append(new_team)
                    players += 1



    def get_random_team(self):
        players = 0
        # todo implement id system for user
        checklist = []
        for i in range(int(self.total_players)):
            while players == i:
                team = Team(random.choice(self.randomlist))
                if team not in checklist:
                    checklist.append(team)
                    self.player.add_team(team)
                    self.players_list.append(team)
                    players += 1

    def play_next_game(self, game_nr):

        first_done = False
        print("\n\nNext game is: \n")
        for team in self.fixtures[game_nr]:
            if first_done is False:
                print(f'{team} VS ', end="")

                first_done = True
            else:
                print(team)
        print("")
        return self.fixtures[game_nr][0], self.fixtures[game_nr][1]


    def get_total_players(self):

        while True:
            players = input("How many players: ")
            if self.validate.validate_integer(players):
                return int(players)


    def get_rounds(self):
        while True:
            try:
                number = int(input("How many rounds you want to play? "))
                if number > 0:
                    return number
            except:
                print("Please enter a number! ")


    def __total_games_per_round__(self):
        return f"{round(((self.total_players*(self.total_players-1))/2))}"


    def create_game(self, team_list):

        game = []
        while len(game) < 2:
            team = random.choice(self.players_list)
            if team not in game:
                game.append(team)

        return game


    def get_fixtures(self):
        counter = 0
        index = 0
        print(f"Total players: {self.total_players}")
        print(self.players_list)
        while counter < (len(self.players_list) / 2):
            self.fixtures[counter] = [self.players_list[index], self.players_list[index + 1]]
            index += 2
            counter += 1


    def print_fixtures(self):

        print("  ---- FIXTURES ----")
        print(f"  ---- You're playing {self.total_rounds} rounds ----")
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



    def __print_starting_info__(self):
        retval = f'\nSo {self.total_players} players are competing.\n'
        retval += f'You wanted to play {self.total_rounds} rounds.\n'
        retval += f'In total you will play {int(self.__total_games_per_round__())*int(self.total_rounds)} games'
        print(retval)
        return retval


    def __str__(self):
        print("\n"+PADDING+"\n\n")

        for i in range(MIDDLE-int(len(self.name)/2)):
            print(" ", end="")


        print(f'{self.name}')

        for i in range(MIDDLE-int(len(self.name)/2)):
            print(" ", end="")
        print("\n")


        print(PADDING, "\n")

        print("{:<18}{:}{:<10}{:}{:<10}"
              "{:}{:<11}{:}{:<6}{:}{:<6}".format("PLAYER",
                                         "", "PLAYED","", "SCORED",
                                         "", "CONCEDED", "", "+/-", "", "POINTS"))

        print("{:<18}{:}{:<6}{:4}{:<7}{:<3}{:<3}{:<3}{:<3}{:<3}{:<3}"
              .format("----------", "",  "------", "",  "------", "","--------", "", "---", "",  "------"))


        # print("PLAYER               PLAYED   SCORED   CONCEDED   +/-  POINTS")
        # print("------               ------   ------   --------   ---  ------")

        sorted_x = sorted(self.players_list, key=operator.attrgetter('points'))
        sorted_x.reverse()

        # print('{:>12.2f}'.format(num))

        retval = ""

        for team in sorted_x:
            retval += "{:<18}".format(team.name)
            retval += "{:3}".format(team.played_games)
            retval += "{:10}".format(team.scored_goals)
            retval += "{:11}".format(team.conceded_goals)
            retval += "{:9}".format(team.scored_goals-team.conceded_goals)
            retval += "{:7}\n".format(team.points)

        return retval
