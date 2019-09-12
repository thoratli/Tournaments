
TOTAL_OPTIONS = 4

class Options:

    def __init__(self):
        self.total_options = TOTAL_OPTIONS

    def show_options(self):
        retval = "\n------------------------\n[ENTER] PLAY NEXT GAME\n------------------------\n"
        retval += "[1] Show fixtures \n"
        retval += '[2] Show table - missing values\n'
        retval += "[3] Print stats - not implemented\n"
        return retval

    def get_option(self):
        option = input("Enter an option: ")
        return option
