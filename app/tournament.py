from app.validation import Validation
from app.team import Team
from app.options import Options
from app.mysqldata import DatabaseSearcher
import random
import getpass
import operator
PADDING = "--------------------------------------------------------------"
MIDDLE = int(len(PADDING)/2)

class Tournament():
    def __init__(self, database, id=None, type=None, name=None, rounds=None, players=None, game_counter=None, players_list=None, new=False):
        self.database = database
        if id:
            self.id = id
        else:
            self.id = None

        if type:
            self.type = type
        else:
            self.type = ""

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

        self.total_games = self.set_total_games()

        self.password = None
        self.options = Options()
        self.validate = Validation()

        if new:
            self.fixtures = {}
        else:
            self.fixtures = self.get_fixtures_from_db()

        self.randomlist = ['Real Madrid', 'Barcelona', 'Liverpool', 'Iceland', 'Brazil',
                           'PSG', '1 star', '2 star', 'Spain', '3 star', '4 star','Lowest star',
                           'Everton', 'Chelsea', 'Basel', 'Manchester City',
                           'IcelanderTeam', 'Manchester United', 'Arsenal', 'Leicester', 'Ajax',
                           'Atletico Madrid', 'Tottenham', 'Bayern Munchen', 'B. Dortmund', 'Juventus',
                           'Roma', 'Inter Milan', 'Colombia', 'England', 'Sweden', 'Scandinavia', 'Italy',
                           'Burnley', 'Sevilla']


    def get_fixtures_from_db(self):
        """Reads the fixtures from database """
        database = DatabaseSearcher()
        self.fixtures = database.get_fixtures(self.id)

    def get_password(self):
        """Gets the passwords from user and returns it"""
        #todo: implement hashing
        #todo: implement sending the password to email
        #todo: implement recover on password

        while True:
            password = getpass.getpass(prompt="Enter a easy password for later access: ")
            password2 = getpass.getpass(prompt="Repeat your password:")
            if password == password2:
                print("Remember: ", password)
                self.password = password
                return password
            else:
                print("Didn't match. Try again: ")

    def set_total_games(self):
        self.total_games = int(self.total_rounds) * int(self.__total_games_per_round__())
        return self.total_games

    def get_type(self):
        """Gets the type of sport from menu options. Returns the type"""
        print(f"[1] Soccer/Fifa/PES\n[2] UFC\n[3] Darts")
        type = input().strip()
        if type in '123':
            if type == '1':
                self.type = 'Soccer'
            elif type == '2':
                self.type = 'UFC'
            else:
                self.type = 'Darts'

        return self.type


    def get_form(self):
        """Gets the form the user. If the form is one random team throughout the
        league its assignes teams and returns the random_team list. Else it returns an empty list"""

        self.print_random_teamlist(6)

        play_random = input(f"You want to play with a fixed random team from our list [Y/n]: ")

        if play_random in "yY ":
            #Búa til lista með random liðum
            rand_teams = self.get_random_teams()


            # Prenta út hver er hvaða lið
            self.print_assigned_teams(self.players_list, rand_teams)

            # self.get_random_team() # commeentaði þetta út í bili.
            for i in range(self.total_players):
                # todo: capitalize rand_teams[i] in the string
                self.players_list[i].name += " " + "(" + rand_teams[i] + ")" # Bæti hér við random liðinu fyrir aftan nafnið á spilaranum.

            return rand_teams
        else:
            return []

    def random_every_game(self):
        """Offers the user to play with random team per round, returns
        random team if he wants, else returns False"""

        random_team_choice = input("\nYou want us to choose random teams for every game? [Y/n]:")
        if random_team_choice in "Yy ":
            return random_team_choice # Returning this string if user wants random teams every game
        else:
            return False# Returning nothing if user chooses not to have random teams every game

    def get_tournament_name(self):
        """Returns the input of the tournament name"""
        name = input("What is the name of your League: ")
        self.name = name
        return name

    def get_total_players(self):
        """Allows participants to enter number of competitors """

        while True:
            players = input("How many players: ")
            if self.validate.validate_integer(players):
                players = int(players)
                if self.validate.validate_limit(players, 2):
                    self.total_players = players
                    return int(players)

    def get_rounds(self):
        """Allows user to enter the number of rounds they want to play
        and returns that number"""

        while True:
            number = input("How many rounds you want to play? ")
            if self.validate.validate_integer(number):
                if self.validate.validate_limit(number, 1):
                    self.total_rounds = int(number)
                    return int(number)

    def play_next_game(self, tournament_id, game_counter):
        """Plays the next game and returns the fixtures"""
        print("Next game is: \n")

        for game_number, value in self.fixtures.items():
            game = value[0]
            home, away = game
            # played = value[1]
            played = self.database.is_played(tournament_id, game_number)
            if not played:
                self.database.updated_played(tournament_id, game_number)
                if home.name != 'Day Off' and away.name != 'Day Off':
                    print(home, "VS", away, end=" ")
                    return home, away

        #Should not reach here
        return home, away

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
                randlist.append(random_team.capitalize())
                counter += 1
        return randlist

    def __total_games_per_round__(self):
        """Returns total games per round"""
        return f"{round(((self.total_players*(self.total_players-1))/2))}"

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

    def get_winner(self):
        """Winner is decided by points but secondary decided on goal difference"""
        max = 0
        maxdiff_origin = 0
        goal_difference = False

        counter = 0
        for index, i in enumerate(self.players_list):
            print("INDEXAR: ", index)
            if i.name != 'Day Off':
                curr_diff = int(i.scored_goals) - int(i.conceded_goals)
                print("TEAM:", i.name, "DIFFERENCE:", curr_diff)
                if int(i.points) > max:
                    max = int(i.points)
                    name = str(i.name)


                elif int(i.points) == max:
                    if curr_diff > maxdiff_origin:
                        max = int(i.points)
                        name = str(i.name)
                        maxdiff_origin = curr_diff
                        goal_difference = True

                else:
                    tied = True

        if goal_difference:
            return f'{name} with {str(max)} points, on GOAL DIFFERENCE!'
        return f'{name} with {str(max)} points'

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

        sorted_x = sorted(self.players_list, key=operator.attrgetter('points'))
        sorted_x.reverse()
        retval = ""

        for team in sorted_x:
            if team.name != "Day Off":
                retval += "{:<27}".format(team.name).capitalize()
                retval += "{:3}".format(team.played_games).capitalize()
                retval += "{:10}".format(team.scored_goals).capitalize()
                retval += "{:11}".format(team.conceded_goals).capitalize()
                retval += "{:9}".format(team.scored_goals-team.conceded_goals).capitalize()
                retval += "{:7}\n".format(team.points).capitalize()

        return retval
