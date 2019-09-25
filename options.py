
TOTAL_OPTIONS = 5

class Options:

    def __init__(self):
        self.total_options = TOTAL_OPTIONS

    def show_options(self):
        retval = "\n------------------------\n[ENTER] PLAY NEXT GAME\n------------------------\n"
        retval += "[1] Show fixtures \n"
        retval += '[2] Show table \n'
        retval += "[3] Print stats - not implemented\n"
        retval += "[4} Leave application \n"
        return retval

    def get_option(self):
        option = input("Enter an option: ").strip()
        return option


    def show_stat_options(self):
        retval = "[1] Biggest Win \n"
        retval += '[2] Biggest loss \n'
        retval += "[3] Most games won in a row\n"
        retval += "Any other suggestions? email us, t@tourno.sick\n"
        return retval

