class Tournament:
    def __init__(self):
        self.rounds = 0
        self.players = 0



    def get_players(self):
        while True:
            try:
                self.players = int(input("How many players will participate? "))
                return
            except:
                print("Please enter a number: ")


        pass

    def get_games(self):
        # Todo: implement
        pass

    def get_rounds(self):
        # Todo: implement
        pass
