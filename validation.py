#toDo: atli implement validation class

class Validation():

    def validate_integer(self, string: str):

        try:
            int(string)
            return True
        except:
            print("Please enter an integer! ")
            return False


    def validate_score_input(self, string: str):
        pass

    def validate_name_input(self, string: str):
        namelist = string.split()
        if len(namelist) == 1:
            return True
        else:
            print("Please, just one name! ")
            return False

    def validate_rounds(self, integer: int):
        pass

