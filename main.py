from tournament import Tournament
# from options import Options
from validation import *
from Files.mysqldata import DatabaseSearcher
import time
from game import Game
from team import Team

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
    validate = Validation()
    option = Options()

    print("[1] Play a new game")
    print("[2] Continue with a league")

    users_pick = input("Enter choice: ")

    if users_pick == '1':
        new_game = Tournament()
        random_team = new_game.__initial_tournament__()
        new_game.get_fixtures()
        new_game.__print_starting_info__()
        total_games = int(new_game.__total_games_per_round__())*int(new_game.total_rounds)
        game_counter = new_game.game_counter
        game_players = Team()


    elif users_pick == '2':
        print("\nReading from database....")
        time.sleep(2)
        print("\n", "\nAvailable leagues:")
        Database = DatabaseSearcher()
        Database.print_available_leagues()

        while True:
            id = input("Enter the ID for the league you want to play? ")
            if Database.get_tournament_by_id(id):
                name, players, rounds, game_counter = Database.get_tournament_by_id(id)
                print("LeagueName:",name,"\nTotal Players: ", players, "\nTotal Rounds: ", rounds)
                players_dict = Database.get_players_data(id, players)
                print("List of players: ", players_dict)
                break

        while True:
            password = input("Enter password or q to quit application: ")

            if password in "Qq":
                quit()

            if Database.validate_password(id, password) is True:
                print("Collecting data from database ...")
                time.sleep(2)


                new_game = Tournament(name, rounds, players, game_counter)
                new_game.set_players_name(players_dict)

                print("nr of players: ", players)
                print("Total rounds: ", rounds)
                print("------------------")
                total_games = int(new_game.__total_games_per_round__()) * int(new_game.total_rounds)
                # random_team
                # random_team = new_game.__initial_tournament__()

                #get the form from the database
                # if form is randomTeams team = Liverpool blabla

                break
            else:
                print("Incorrect password! Try again!!")


    else:
        exit("You don´t deserve us")


    while game_counter < total_games:
        new_game.game_counter += 1
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




