#toDo: atli implement validation class
from options import Options

class Validation():
    def __init__(self):
        self.options = Options()

    def integer(self, string: str):
        """ Validates if parameter is integer and return True, otherwise False """
        try:
            int(string)
            return True
        except:
            print("\nPlease enter an integer!\n")
            return False

    def scores(self, score):
        """ Validates the parameter score and returns True if """
        try:
            home, away = score.split()
            home = int(home)
            away = int(away)
            if home >= 0 and away >= 0:
                return True
            print("This can´t be correct! ")
        except:
            print('\n\nThis didn\'t work. Try again!!')
            return False

    def limit(self, number, min, max=None):
        """Validates upper and lower limits on input"""
        if number == "":
            return True

        try:
            number = int(number)
        except:
            return False

        if max:
            if number <= max:
                if number >= min:
                    return True

                else:
                    print(f"\nThe lowest number available is {min}.")
            else:
                print(f"\nThe highest number available is {max}.")
                return False


        if number < min:
            print(f"\nThe lowest number available is {min}.")
            return False

        return True


    def options(self, option):
        """Validates options and returns the options if it´s acceptable"""

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
            return False
