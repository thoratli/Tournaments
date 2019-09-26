from validation import Validation
from team import Team
from options import Options
import random
import operator
PADDING = "--------------------------------------------------------------"
MIDDLE = int(len(PADDING)/2)

class Tournament():
    def __init__(self, name=None, rounds=None, players=None, game_counter=None, players_list=None):
        if name:
            self.name = name
        else:
            self.name = ""

        if rounds:
            self.total_rounds = rounds
        else:
            self.total_rounds = 0

        if players:
            self.total_players = players
        else:
            self.total_players = 0

        if game_counter:
            self.game_counter = game_counter
        else:
            self.game_counter = 0

        if players_list:
            self.players_list = players_list
            for team in players_list:
                self.player = Team(team.name, team.points, team.played_games, team.scored_goals, team.conceded_goals)
        else:
            self.players_list = []


        self.options = Options()
        self.validate = Validation()
        # self.player = Team()
        self.fixtures = {}
        self.randomlist = ['Real Madrid', 'Barcelona', 'Liverpool', 'Iceland', 'Brazil',
                           'PSG', '1 star', '2 star', 'Spain', '3 star', '4 star','Lowest star',
                           'Everton', 'Chelsea', 'Basel', 'Manchester City',
                           'IcelanderTeam', 'Manchester United', 'Arsenal', 'Leicester', 'Ajax',
                           'Atletico Madrid', 'Tottenham', 'Bayern Munchen', 'B. Dortmund', 'Juventus',
                           'Roma', 'Inter Milan', 'Colombia', 'England', 'Sweden', 'Scandinavia', 'Italy',
                           'Burnley', 'Sevilla']

    def get_password(self):
        """Gets the passwords from user and returns it"""
        #todo: implement hashing
        #todo: implement sending the password to email
        #todo: implement recover on password

        while True:
            password = input("Enter a easy password to access the league later: ")
            print("\n", "Your password will be: ",password, "\n")
            password2 = input("Repeat your password:  ")
            if password == password2:
                print("Remember: ", password)
                return password
            else:
                print("Didn't match. Try again: ")

    def __initial_tournament__(self):

        self.name = self.get_tournament_name()
        self.total_players = self.get_total_players()
        self.total_rounds = self.get_rounds()
        self.set_players_name()
        self.password = self.get_password()

        #refactor this shit
        print("\n", PADDING)
        print(f"\n{self.name} is almost ready to start ...\n")
        print(PADDING)

        self.print_random_teamlist(6)

        play_random = input(f"You want to play with one random team from our list [Y/n]: ")

        if play_random in "yY ":
            #Búa til lista með random liðum
            rand_teams = self.get_random_teams()

            # Prenta út hver er hvaða lið
            self.print_assigned_teams(self.players_list, rand_teams)

            # self.get_random_team() # commeentaði þetta út í bili.
            for i in range(self.total_players):
                # todo: capitalize rand_teams[i] in the string
                self.players_list[i].name += " " + "(" + rand_teams[i] + ")" # Bæti hér við random liðinu fyrir aftan nafnið á spilaranum.

            return self.players_list, rand_teams

        elif play_random in "nN":
            random_team_choice = input("\nYou want us to choose random teams for every game? [Y/n]:")
            if random_team_choice in "Yy ":
                return random_team_choice, False # Returning this string if user wants random teams every game
            else:
                return False, False# Returning nothing if user chooses not to have random teams every game
        else:
            print("Please enter Y or N ! ")

    def get_tournament_name(self):
        """Returns the input of the tournament name"""
        return input("What is the name of your League: ")

    def get_total_players(self):
        """Allows participants to enter number of competitors """

        while True:
            players = input("How many players: ")
            if self.validate.validate_integer(players):
                players = int(players)
                if self.validate.validate_limit(players, 2):
                    return int(players)

    def get_rounds(self):
        """Allows user to enter the number of rounds they want to play
        and returns that number"""

        while True:
            number = input("How many rounds you want to play? ")
            if self.validate.validate_integer(number):
                if self.validate.validate_limit(number, 1):
                    return int(number)

    def set_players_name(self, players_dict=None):
        """Allows participants to enter names for themselves"""
        players = 0
        if players_dict:
            for key, value in players_dict.items():
                name = key
                for attr in value:
                    points = attr[0]
                    scored = attr[1]
                    conceded = attr[2]
                    played = attr[3]
                    new_team = Team(name, points, played, scored, conceded)
                    print(new_team)
                    self.players_list.append(new_team)

        else:
            for i in range(int(self.total_players)):
                while players == i:
                    team_name = input(f'Participant nr {players +1}: ')
                    # if self.validate.validate_name_input(team_name):
                    new_team = Team(team_name)
                    self.players_list.append(new_team)
                    players += 1

    def print_assigned_teams(self, players_list, rand_teams):
        """Prints assigned team for each player"""

        print("-- \nHere are the teams assigned for this league --\n")
        for i in range(self.total_players):
            print(f"{str(players_list[i]).capitalize()} -> {rand_teams[i]}\n")

    def get_random_teams(self):
        """Creates a list of random teams of size total players and returns it"""
        randlist = []
        counter = 0
        while counter < self.total_players:
            random_team = random.choice(self.randomlist)
            if random_team not in randlist:
                random_team = random_team.capitalize()
                randlist.append(random_team)
                counter += 1
        return randlist

    def get_random_team(self):
        """Assigns a team to a players from the randomlist """

        players = 0
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
        """Plays the next game and returns the fixtures"""

        first_done = False
        print("\n\nNext game is: \n")
        for team in self.fixtures[game_nr]:
            if first_done is False:
                print(f'{str(team).capitalize()} VS ', end="")

                first_done = True
            else:
                print(str(team).capitalize())
        print("")
        return self.fixtures[game_nr][0], self.fixtures[game_nr][1]

    def __total_games_per_round__(self):
        """Returns total games per round"""

        return f"{round(((self.total_players*(self.total_players-1))/2))}"

    def create_game(self, team_list):
        """Creates a list of games"""

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
        """Returns one fixture from randomlist"""

        while True:
            team1 = random.choice(self.randomlist)
            team2 = random.choice(self.randomlist)
            teams = f'{str(team1).capitalize()} VS {str(team2).capitalize()}'
            return teams

    def print_fixtures(self):
        """Prints all fixtures for tournament"""

        for game,teams in self.fixtures.items():
            print(f"Game nr {game+1}: ", end="")
            number_of_teams = 0
            for team in teams:
                if number_of_teams == 0:
                    print(f"{str(team).capitalize()} ", end="VS ")
                    number_of_teams += 1
                else:
                    print(f"{str(team).capitalize()}", end=" ")
            print("")

    def __print_starting_info__(self):
        """Returns a starting info before the tournament starts"""

        retval = f'So {self.total_players} players are competing.\n'
        retval += f'You wanted to play {self.total_rounds} rounds.\n'
        retval += f'In total you will play {int(self.__total_games_per_round__())*int(self.total_rounds)} games'
        print(retval)
        return retval

    def print_random_teamlist(self, teams_in_one_line):
        """Prints all teams from randomlist"""

        retval = ""
        length = 0

        for i in self.randomlist:
            length += len(i)
            if i == self.randomlist[-1]:
                retval += i
            elif length >= teams_in_one_line*10:
                retval += "\n"
                length = 0
            else:
                retval += f"{i}, "

        print(retval, "\n")

    def __str__(self):
        #todo: Refactor __str__ function for tournament

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
            retval += "{:<27}".format(team.name).capitalize()
            retval += "{:3}".format(team.played_games).capitalize()
            retval += "{:10}".format(team.scored_goals).capitalize()
            retval += "{:11}".format(team.conceded_goals).capitalize()
            retval += "{:9}".format(team.scored_goals-team.conceded_goals).capitalize()
            retval += "{:7}\n".format(team.points).capitalize()

        return retval
