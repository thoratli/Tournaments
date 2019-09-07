

class Tournament:
    def __init__(self):
        self.players_list = []
        self.rounds = 0
        self.players = 0
        self.total_players = self.get_total_players()
        self.total_rounds = self.get_rounds()



    def get_total_players(self):

        while True:
            try:
                self.players = int(input("How many players will participate? "))
                return
            except:
                print("Please enter a number! ")


    def get_players_name(self):


    def __get_names__(self):
        for name in range(self.players):

            self.players_list.append(name)



    def get_rounds(self):
        while True:
            try:
                number = int(input("How many rounds you want to play? "))
                if number > 0:
                    self.players = number
                    return
            except:
                print("Please enter a number! ")