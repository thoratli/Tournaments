# from validation import Validation
from tournament import *

class Options:

    def __init__(self):
        self.total_options = 3

    def show_options(self):
        retval = "\n[1] Print current League\n"
        retval += "[2] Play next game in current Tournament\n"
        retval += "[3] Print stats"
        return retval

    def get_option(self):
        option = input("Enter an option: ")
        return option
