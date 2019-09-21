from tournament import Tournament
# from options import Options
from validation import *
from game import Game
from datareader import abstract_model
from stats import Statistics

SPACE = "                                             "
LINES = "\n-----------------------------------------------\n"
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

def freeze_screen():
    input("\nPRESS ANY KEY TO CONTINUE")


def main():

    print(f'{PADDING}\n{WELCOME}\n{PADDING}')
    game_counter = 0

    print("[1] Play a new game")
    print("[2] Continue with a league")

    users_pick = input("Enter choice: ")

    if users_pick == '1':
        option = Options()
        new_game = Tournament()
        validate = Validation()

        random_team = new_game.__initial_tournament__()
        new_game.get_fixtures()
        new_game.__print_starting_info__()
        total_games = int(new_game.__total_games_per_round__())*int(new_game.total_rounds)

    # elif users_pick == '2':
    #     print("Reading from database....")
    #     database = abstract_model()



    else:
        exit("You don´t deserve us")


    while game_counter < total_games:
        print(option.show_options())

        the_option = option.get_option()
        if validate.validate_limit(the_option, 1, 4) or the_option == "":
            if the_option == '':
                dict_key = game_counter%int(new_game.__total_games_per_round__())
                print(LINES)
                home, away = new_game.play_next_game(dict_key)

                if isinstance(random_team, str) and random_team in 'Yy':
                    print(new_game.get_one_fixture() + "\n")

                while True:
                    print(LINES)

                    score = input("Enter results, two integers with space between: ")
                    if validate.validate_score_input(score):
                        score = score.split()
                        a_game = Game(score[0], score[1], home, away)
                        a_game.handle_scores()
                        game_counter += 1
                        break

            elif the_option == '1':
                print(LINES)
                print(f"           ~~~~~ {new_game.name} ~~~~~")
                print(f'\nYou are playing {new_game.total_rounds} rounds of the following games')
                print(LINES)

                #todo: print only unplayed games or games with scores
                new_game.print_fixtures()
                print(LINES)
                freeze_screen()


            elif the_option == '2':
                print(new_game)
                freeze_screen()

            elif the_option == '3':

                print(option.show_stat_options())
                stat_option = input("Pick your stat: ")

                if stat_option == '1':
                    print("Biggest Win(Jóhannes): X vs Y, 5 - 1.")

                elif stat_option == '2':
                    print("Biggest loss(Birnir): X vs Y, 5 - 1.")

                elif stat_option == '3':
                    print("Most games won in a row(Þórarinn): 6")

                else:
                    print("NOT AN OPTION!! ")

                freeze_screen()




            elif the_option == '4':
                print('You can´t leave us BITCH! ')
                freeze_screen()
                #todo: implement write out
                #writeout function
                #quic

    # the end of the loop, it shows the league standings
    print(new_game)




main()




