from tournament import Tournament
from options import Options
from validation import *
from Play import *


WELCOME = "########## ########  ##    ##  #########   ##   ##     ####         ###       ###      #########  ##   ##   ##########\n" \
          "    ##     ##    ##  ##    ##  ##     ##   ###  ##    ##  ##       ## ##     ## ##     ##         ###  ##       ##    \n" \
          "    ##     ##    ##  ##    ##  #########   ##  ###   ########     ##   ##   ##   ##    #########  ##  ###       ##    \n" \
          "    ##     ##    ##  ##    ##  ##      ##  ##   ##  ##      ##   ##     ## ##     ##   ##         ##   ##       ##    \n" \
          "    ##     ########  ########  ##      ##  ##   ## ##        ## ##       ###       ##  #########  ##   ##       ##    \n" \
          "\n" \
          "\n" \
          "                 ### ###   #### ####  ##### ## ##  ##     ######  ##  ##  ####   ###   ###  ##### #####  ####\n" \
          "  ###########    ### #     ##   ##    ## ## ## ### ##       ##    ##  ##  ##    ##    ##    ## ## ## ##  ##  \n" \
          "  ###########    ####      #### ####  ##### ## ## ###       ##    ######  ####    #  ##     ## ## #####  ####\n" \
          "                 ### #     ##   ##    ##    ## ##  ##       ##    ##  ##  ##     ##   ##    ## ## ##  #  ##  \n" \
          "                 ###  ###  #### ####  ##    ## ##  ##       ##    ##  ##  ####  ##     ##   ##### ##   # #### \n"

def main():
    option = Options()
    new_game = Tournament()
    validate = Validation()
    print(WELCOME)
    Tournament_finished = False
    #todo: implement the main function so it show options and depending on option it will do something

    new_game.__initial_tournament__()
    new_game.__print_starting_info__()

    while Tournament_finished is False:

        print(option.show_options())
        the_option = option.get_option()
        if validate.validate_options(the_option):

            if the_option == '1':
                print(f'Standings for {new_game.name}')
                new_game.print_league()


            elif the_option == '2':
                print(f'\nOPTION {the_option}\n for PLAYING')


            elif the_option == '3':
                print(f'\nOPTION {the_option}\nThe stats are not implemented yet, sorry!')




main()




