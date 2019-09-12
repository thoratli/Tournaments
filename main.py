from tournament import Tournament
from options import Options
from validation import *
from Play import *
from game import Game

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

                new_game.play_next_game(game_counter)

                while True:
                    score = input("How did it end: (2 2)")
                    a_game = Game()

                    if validate.validate_score_input(score):
                        score = score.split()
                        the_game = new_game.fixtures[game_counter]

                        a_game = Game(score[0], score[1], the_game[0], the_game[1])

                        a_game.handle_scores()
                        break


                game_counter += 1


                #todo: implement "play_next_game_function"


            elif the_option == '1':
                print(f'\nUpcoming games for {new_game.name}')
                #todo: print only unplayed games or games with scores
                new_game.print_fixtures()


            elif the_option == '2':
                print(new_game)


            elif the_option == '3':
                print(f'\nOPTION {the_option}\nThe stats are not implemented yet, sorry!')


    #the end of the loop, it shows the league standings
    new_game.print_league()


main()




