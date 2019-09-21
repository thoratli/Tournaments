import csv
TOURNAMENT_NAME = 0
ID = 1
ROUNDS = 2
TOTAL_PLAYERS = 3
PLAYER_NAME = 4
FORM = 5
TEAM = 6
PLAYED = 7
SCORED = 8
CONCEDED = 9
DIFFERENCE = 10
POINTS = 11


class abstract_model():
    def __init__(self):
        self.file_list = []
        self.tournaments = {}
        self.players_data = {}



    def read_data(self,filename):
        """Reads data from given csvfile"""

        with open(filename, 'r', encoding='utf-8-sig', newline='') as src:
            reader = csv.reader(src, dialect='excel')

            for row in reader:
                self.file_list.append(row)


    def print_data(self):


        self._print_headers()
        for index, value in enumerate(self.file_list[1:]):
            print(value)
        #     id = (value[index+1])
        #     if id not in listinn:
        #         listinn.append(id)
        #         count_values += 1
        #
        # print(count_values)
        # print(len(listinn))


            # print(leaguename + " Id: ", id)


    def _print_headers(self):
        for value in self.file_list[0]:
            print(value, end=" ")
        print("\n")

    def get_tournament_data(self):

        # total_players = self.get_total_players()
        print("---------------------------------------------------------\n")
        print("These are the Tournaments in the database with all data:\n")
        print("---------------------------------------------------------\n")

        # self._print_headers()

        tournament_number = 1

        # starting from 1 row to skip headers
        for row in self.file_list[1:]:
            #information for the tournament
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
            self.tournaments[id] = [id]
            self.tournaments[id].append(name)
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

    def print_tournament_data(self):

        #prints out the Tournament ID and its data
        for key,value in self.tournaments.items():
            print("Tournament ID:", key, ",Tournament data:", value)
        print("\n")

    def print_player_data(self):
        #prints out each player and his attributes
        for key,value in self.players_data.items():
            print("Player:", key, " Attributes:", value)


model = abstract_model()
read = model.read_data('data.csv')
model.get_tournament_data()
model.print_tournament_data()
model.print_player_data()