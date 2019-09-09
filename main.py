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
    game_counter = 0

    #initializing tournament and get data for it
    new_game.__initial_tournament__()
    new_game.__print_starting_info__()

    while game_counter < int(new_game.total_games()):

        print(option.show_options())

        the_option = option.get_option()
        if validate.validate_options(the_option):

            if the_option == '1':
                new_game.print_league()

            elif the_option == '2':
                print(f'\nUpcoming games for league: {new_game.name}')
                #todo: implement fixture feature


            elif the_option == '3':
                # print(f'\nNext game is x x')
                # next game from tournament.next_fixture
                # play.play_next_game(new_game.total_games())

                game_counter += 1

                #todo: implement "play_next_game_function"


            elif the_option == '4':
                print(f'\nOPTION {the_option}\nThe stats are not implemented yet, sorry!')


    #the end of the loop, it shows the league standings
    new_game.print_league()


main()




