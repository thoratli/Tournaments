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

    def validate_score_input(self):

        while True:
            try:
                score = input("Enter the score: 2 2").strip().split()
                if len(score) ==2:
                    return int(score[0]), int(score[1])
                else:
                    print("Please try again! Enter 2 numbers with space between!")
            except:
                print("Please try again! x x")

    def validate_name_input(self, string: str):
        namelist = string.split()
        if len(namelist) == 1:
            return True
        else:
            print("Please, just one name! ")
            return False

    def validate_rounds(self, integer: int):
        pass

    def validate_options(self, option):

        try:
            option = int(option)
            if 0 < option <= self.options.total_options:
                return True
            print("You had 1 task! To pick from 3 numbers! PLEASE STAY FOCUSED")
            return False
        except:
            print("Integer! Please!")
