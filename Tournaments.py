

class Tournament:
    def __init__(self):
        self.players_list = {}
        self.rounds = 0
        self.players = 0
        self.total_players = self.__get_total_players__()
        self.total_rounds = self.__get_rounds__()
        self.players_list = self.__get_players_name__()
        print(self.__print_starter__())



    def __get_total_players__(self):

        while True:
            try:
                self.players = int(input("How many players will participate? "))
                return self.players
            except:
                print("Please enter a number! ")


    def __get_players_name__(self):

        for i in range(int(self.total_players)):
            self.players_list[i+1] = input(f'Participant nr {i+1}: ')


    def __get_names__(self):
        for name in range(self.players):

            self.players_list.append(name)


    def __get_rounds__(self):
        while True:
            try:
                number = int(input("How many rounds you want to play? "))
                if number > 0:
                    return number
            except:
                print("Please enter a number! ")


    def __total_games__(self):
        return f'{(round(self.total_players/2)*(self.total_players-1))}'


    def __print_starter__(self):
        retval = f'So {self.total_players} players are competing.\n'
        retval += f'You wanted to play {self.total_rounds} rounds.\n'
        retval += f'In total you will play {self.__total_games__()} games'
        return retval