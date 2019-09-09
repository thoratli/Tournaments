# from validation import Validation
from tournament import *

class Options:
    def __init__(self):
        self.show_options()

    def show_options(self):
        retval = "\n\n[1] Create Tournament\n"
        retval += "[2] Print current League\n"
        retval += "[3] Play next game in current Tournament"
        return retval