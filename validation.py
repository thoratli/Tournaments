#toDo: atli implement validation class
from options import Options

class Validation():
    def __init__(self):
        self.options = Options()

    def validate_integer(self, string: str):

        try:
            int(string)
            return True
        except:
            print("Please enter an integer! ")
            return False

    def validate_score_input(self, score):

        try:
            home, away = score.split()
            home = int(home)
            away =int(away)
            if home > 0 and away > 0:
                return True
            print("This can´t be correct! ")
        except:
            print("\n\nThis didn't work. Try again!!")
            return False


    def validate_rounds(self, rounds):
        if int(rounds) > 0:
            return True
        print("The lowest number available is 1.")
        return False



    def validate_options(self, option):

        try:
            if option == '':
                return option
            option = int(option)
            if 0 < option <= self.options.total_options:
                return True
            print("You had 1 task! To pick from 3 numbers! PLEASE STAY FOCUSED")
            return False
        except:
            print("Integer! Please!")
