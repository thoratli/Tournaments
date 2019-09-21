from tournament import Tournament
from options import Options
from validation import *
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
    print(f'{PADDING}\n{WELCOME}\n{PADDING}')
    game_counter = 0
    random_team = new_game.__initial_tournament__()
    new_game.get_fixtures()
    new_game.__print_starting_info__()
    total_games = int(new_game.__total_games_per_round__())*int(new_game.total_rounds)

    while game_counter < total_games:

        print(option.show_options())
        the_option = option.get_option()
        if validate.validate_limit((the_option), 1, 3) or the_option == "":
            if the_option == '':
                dict_key = game_counter%int(new_game.__total_games_per_round__())
                home, away = new_game.play_next_game(dict_key)

                if isinstance(random_team, str) and random_team in 'Yy':
                    print(new_game.get_one_fixture() + "\n")

                while True:
                    score = input("How did it end: (2 2): ")

                    if validate.validate_score_input(score):
                        score = score.split()
                        a_game = Game(score[0], score[1], home, away)
                        a_game.handle_scores()
                        game_counter += 1
                        break

            elif the_option == '1':
                print(f'\nYou are playing {new_game.total_rounds} rounds')
                #todo: print only unplayed games or games with scores
                new_game.print_fixtures()


            elif the_option == '2':
                print(new_game)

            elif the_option == '3':
                print(f'\nOPTION {the_option}\nThe stats are not implemented yet, sorry!')


    #the end of the loop, it shows the league standings
    print(new_game)


main()




