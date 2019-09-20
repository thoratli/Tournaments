from validation import Validation
from team import Team
from options import Options
import random
import operator
PADDING = "--------------------------------------------------------------"
MIDDLE = int(len(PADDING)/2)

class Tournament():
    def __init__(self):
        self.options = Options()
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
        self.set_players_name()

        #refactor this shit
        while True:
            play_random = input(f"You want to have one random team throughout the -- {self.name} -- league [Y/n]: ").lower()
            if play_random in 'yY ':
                #Búa til lista með random liðum
                rand_teams = self.get_random_teams()

                # Prenta út hver er hvaða lið
                self.print_assigned_teams(self.players_list, rand_teams)


                # self.get_random_team() # commeentaði þetta út í bili.
                for i in range(self.total_players):
                    self.players_list[i].name += " " + "(" + rand_teams[i] + ")" # Bæti hér við random liðinu fyrir aftan nafnið á spilaranum.
                return self.players_list

            elif play_random in 'nN':
                random_team_choice = input("\nYou want us to choose random teams for every game? [Y/n]: ")
                if random_team_choice in "Yy":
                    return random_team_choice # Returning this string if user wants random teams every game
                else:
                    return # Returning nothing if user chooses not to have random teams every game
            else:
                print("Please enter Y or N ! ")


    def print_assigned_teams(self, players_list, rand_teams):
        print("-- Here are the teams assigned for this league --")
        print("")
        for i in range(self.total_players):
            print(f"{players_list[i]} -> {rand_teams[i]}")
            print("")



    def get_random_teams(self):
        randlist = []
        counter = 0
        while counter < self.total_players:
            random_team = random.choice(self.randomlist)
            if random_team not in randlist:
                randlist.append(random_team)
                counter += 1
        return randlist




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
                if int(players) <= 1:
                    print("You can´t play a tournament on your own. Call your friends! ")
                if int(players) > 1:
                    return int(players)


    def get_rounds(self):
        while True:
            try:
                number = int(input("How many rounds you want to play? "))
                if number > 0:
                    return number
                else:
                    print("Please enter a number >0 ! ")
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

        checklist = []
        counter = 0
        while counter < int(self.__total_games_per_round__()):
            game = self.create_game(self.players_list)

            if game not in checklist:
                checklist.append(game)
                self.fixtures[counter] = game
                counter += 1

    def get_one_fixture(self):

        while True:
            team1 = random.choice(self.randomlist)
            team2 = random.choice(self.randomlist)


            teams = f'{team1} VS {team2}'
            return teams


            # happy = input("Are you happy with the teams? [Y/n] \n")
            #
            # if happy in 'Yy ':
            #     return teams
            # else:
            #     print("\nCry me a river, We will give you new teams ... \n")


    def print_fixtures(self):

        print("  ---- FIXTURES ----")
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

        print("{:<27}{:}{:<10}{:}{:<10}"
              "{:}{:<11}{:}{:<6}{:}{:<6}".format("PLAYER",
                                         "", "PLAYED","", "SCORED",
                                         "", "CONCEDED", "", "+/-", "", "POINTS"))

        print("{:<27}{:}{:<6}{:4}{:<7}{:<3}{:<3}{:<3}{:<3}{:<3}{:<3}"
              .format("----------", "",  "------", "",  "------", "","--------", "", "---", "",  "------"))


        # print("PLAYER               PLAYED   SCORED   CONCEDED   +/-  POINTS")
        # print("------               ------   ------   --------   ---  ------")

        sorted_x = sorted(self.players_list, key=operator.attrgetter('points'))
        sorted_x.reverse()

        # print('{:>12.2f}'.format(num))

        retval = ""

        for team in sorted_x:
            retval += "{:<27}".format(team.name)
            retval += "{:3}".format(team.played_games)
            retval += "{:10}".format(team.scored_goals)
            retval += "{:11}".format(team.conceded_goals)
            retval += "{:9}".format(team.scored_goals-team.conceded_goals)
            retval += "{:7}\n".format(team.points)

        return retval
