import csv

#These are the rows in the CSV
TOURNAMENT_NAME = 0
ID = 1
ROUNDS = 2
TOTAL_PLAYERS = 3
FORM = 4
PLAYER_NAME = 5
TEAM = 6
PLAYED = 7
SCORED = 8
CONCEDED = 9
DIFFERENCE = 10
POINTS = 11

#print the first 4 cols from csv
HEADER_FOR_TOURNAMENT_LOWER = 0
HEADER_FOR_TOURNAMENT_HIGHER = 4

#print the last rows from cols
HEADER_PLAYERS_LOWER = 5
HEADER_PLAYERS_HIGHER = 10


class abstract_model():
    def __init__(self, filename):
        self.file_name = filename
        self.file_list = []
        self.tournaments = {}
        self.players_data = {}

    def get_all_data(self, key_in):

        attribute_list = []
        for key,value in self.tournaments.items():
            if int(key) == int(key_in):
                name = value[TOURNAMENT_NAME]
                id = value[ID]
                rounds = value[ROUNDS]
                total_players = value[TOTAL_PLAYERS]
                form = value[FORM]

                attribute_list.append(name)
                attribute_list.append(id)
                attribute_list.append(rounds)
                attribute_list.append(total_players)
                attribute_list.append(form)

                return attribute_list

        # return self.tournaments[key], self.players_data[key]

    def read_data(self):
        """Reads data from given csvfile"""

        with open(self.file_name, 'r', encoding='utf-8-sig', newline='') as src:
            reader = csv.reader(src, dialect='excel')

            for row in reader:
                self.file_list.append(row)

    def get_tournament_data(self):

        tournament_number = 1

        # starting from 1 row to skip headers
        for row in self.file_list[1:]:
            name = self.file_list[tournament_number][TOURNAMENT_NAME]
            id = self.file_list[tournament_number][ID]
            rounds = self.file_list[tournament_number][ROUNDS]
            total_players = self.file_list[tournament_number][TOTAL_PLAYERS]
            form = self.file_list[tournament_number][FORM]

            player_name = self.file_list[tournament_number][PLAYER_NAME]
            team = self.file_list[tournament_number][TEAM]
            played = self.file_list[tournament_number][PLAYED]
            scored = self.file_list[tournament_number][SCORED]
            conceded = self.file_list[tournament_number][CONCEDED]
            goal_difference = self.file_list[tournament_number][DIFFERENCE]
            points = self.file_list[tournament_number][POINTS]

            #entering the data into the dict
            self.tournaments[id] = []
            self.tournaments[id].append(name)
            self.tournaments[id].append(id)
            self.tournaments[id].append(rounds)
            self.tournaments[id].append(total_players)
            self.tournaments[id].append(form)

            #assigning data to the players
            self.players_data[player_name] = []
            self.players_data[player_name].append(id)
            self.players_data[player_name].append(team)
            self.players_data[player_name].append(played)
            self.players_data[player_name].append(scored)
            self.players_data[player_name].append(conceded)
            self.players_data[player_name].append(goal_difference)
            self.players_data[player_name].append(points)

            tournament_number += 1

    def _print_headers_for_data(self, minlimit: int, maxlimit: int):
        """Prints out the headers of the csv file, minlimit 4 for tournament,
        minlimit 5 for players and maxlimit 10"""

        print("                        ", end="")
        for index, value in enumerate(self.file_list[0]):
            if minlimit <= index <= maxlimit:
                print("", value, end=" ")
        print("\n")

    def print_tournament_data(self):
        """Prints out tournament data from database"""

        print("---------------------------------------------------------\n")
        print("These are the Tournaments in the database with all data:\n")
        print("---------------------------------------------------------\n")

        self._print_headers_for_data(HEADER_FOR_TOURNAMENT_LOWER, HEADER_FOR_TOURNAMENT_HIGHER)

        for key,value in self.tournaments.items():
            print("Tournament:",key, ", Data:", value)

    def print_player_data(self):
        """Prints out players data from database"""

        print("---------------------------------------------------------\n")
        print("These are the Players in the database with all data:\n")
        print("---------------------------------------------------------\n")

        self._print_headers_for_data(HEADER_PLAYERS_LOWER,HEADER_PLAYERS_HIGHER)


        for key,value in self.players_data.items():
            print("Player:", key, " Attributes:", value)


# model = abstract_model()
# read = model.read_data('data.csv')
# model.get_tournament_data()
# model.print_tournament_data()
# model.print_player_data()