from tournament import Tournament
from options import Options
from validation import *
from Play import *

SPACE = "                                             "

PADDING = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

WELCOME = f"{SPACE}########## ########  ##    ##  #########   ##   ##     ####         ###       ###      #########  ##   ##   ##########\n" \
          f"{SPACE}    ##     ##    ##  ##    ##  ##     ##   ###  ##    ##  ##       ## ##     ## ##     ##         ###  ##       ##    \n" \
          f"{SPACE}    ##     ##    ##  ##    ##  #########   ##  ###   ########     ##   ##   ##   ##    #########  ##  ###       ##    \n" \
          f"{SPACE}    ##     ##    ##  ##    ##  ##      ##  ##   ##  ##      ##   ##     ## ##     ##   ##         ##   ##       ##    \n" \
          f"{SPACE}    ##     ########  ########  ##      ##  ##   ## ##        ## ##       ###       ##  #########  ##   ##       ##    \n" \
          f"{SPACE}\n" \
          f"{SPACE}\n" \
          f"{SPACE}                 ### ###   #### ####  ##### ## ##  ##     ######  ##  ##  ####     ###   ### ##### #####  ####\n" \
          f"{SPACE}  ###########    ### #     ##   ##    ## ## ## ### ##       ##    ##  ##  ##      ##    ##   ## ## ## ##  ##  \n" \
          f"{SPACE}  ###########    ####      #### ####  ##### ## ## ###       ##    ######  ####      #  ##    ## ## #####  ####\n" \
          f"{SPACE}                 ### #     ##   ##    ##    ## ##  ##       ##    ##  ##  ##       ##   ##   ## ## ##  #  ##  \n" \
          f"{SPACE}                 ###  ###  #### ####  ##    ## ##  ##       ##    ##  ##  ####    ##     ##  ##### ##   # #### \n"

def main():
    option = Options()
    new_game = Tournament()
    validate = Validation()
    play = Play()
    print(PADDING)
    print(WELCOME)
    print(PADDING)
    game_counter = 0

    #initializing tournament and get data for it
    new_game.__initial_tournament__()
    new_game.get_fixtures()
    new_game.__print_starting_info__()

    while game_counter < int(new_game.__total_games_per_round__()):

        print(option.show_options())

        the_option = option.get_option()
        if validate.validate_options(the_option) or the_option == "":
            if the_option == '':
                # print(f'\nNext game is x x')
                # next game from tournament.next_fixture
                new_game.play_next_game(game_counter)

                game_counter += 1

                #todo: implement "play_next_game_function"


            elif the_option == '1':
                print(f'\nUpcoming games for {new_game.name}')
                # new_game.get_fixtures()
                new_game.print_fixtures()


            elif the_option == '2':
                new_game.print_league()


            elif the_option == '3':
                print(f'\nOPTION {the_option}\nThe stats are not implemented yet, sorry!')


    #the end of the loop, it shows the league standings
    new_game.print_league()


main()




