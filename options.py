
TOTAL_OPTIONS = 4

class Options:

    def __init__(self):
        self.total_options = TOTAL_OPTIONS

    def show_options(self):
        retval = f'\n[1] Show table'
        retval += "\n[2] Show fixtures \n"
        retval += "[3] Play next game in current Tournament\n"
        retval += "[4] Print stats"
        return retval

    def get_option(self):
        option = input("Enter an option: ")
        return option
