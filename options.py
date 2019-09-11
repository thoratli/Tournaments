
TOTAL_OPTIONS = 4

class Options:

    def __init__(self):
        self.total_options = TOTAL_OPTIONS

    def show_options(self):
        retval = "\n[1][ENTER] PLAY NEXT GAME\n"
        retval += "[2] Show fixtures \n"
        retval += '[3] Show table - missing values\n'
        retval += "[4] Print stats - not implemented\n"
        return retval

    def get_option(self):
        option = input("Enter an option: ")
        return option
