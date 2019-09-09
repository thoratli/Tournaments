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
    print("-----------")
    option = Options()
    new_game = Tournament()
    validate = Validation()
    play = Play()
    print(WELCOME)
    Tournament_finished = False

    #initializing tournament and get data for it
    new_game.__initial_tournament__()
    new_game.__print_starting_info__()

    while Tournament_finished is False:

        print(option.show_options())
        the_option = option.get_option()
        if validate.validate_options(the_option):

            if the_option == '1':
                new_game.print_league()

            elif the_option == '2':
                print(f'\nUpcoming games for league: {new_game.name}')
                #todo: implement fixture feature


            elif the_option == '3':
                print(f'\nNext game is x x')
                while True:
                    scores = play.get_scores_from_input()
                    if validate.validate_score_input(scores):
                        home, away = play.convert_score_string_to_numbers(scores)
                        break

                #todo: implement "play_next_game_function"


            elif the_option == '4':
                print(f'\nOPTION {the_option}\nThe stats are not implemented yet, sorry!')




main()




