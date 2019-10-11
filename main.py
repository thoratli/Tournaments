from tournament import Tournament
# from options import Options
from validation import *
from mysqldata import DatabaseSearcher
import time
from game import Game
from fixtures import Fixtures
from team import Team

SPACE = "                                             "
LINES = "-----------------------------------------------\n"
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

def print_message(message:str, newlines=1):
    newline = "\n"*newlines
    print(message, newline)

def freeze_screen(sleep_time:int, message=None, newlines=1):
    newline = "\n"*newlines

    if message:
        print(str(message),newline)
        time.sleep(sleep_time)
    else:
        input("\nPRESS ANY KEY TO CONTINUE")

def initialize():
    print(f'{PADDING}\n{WELCOME}\n{PADDING}')

def main():
    # initialize instances and print intro.
    #todo: make sure you only print intro (def initalize) once
    database = DatabaseSearcher()
    validate = Validation()
    option = Options()
    initialize()

    #first menu
    print_message("[1] Play a new game\n[2] Continue with a league")

    while True:
        users_pick = input("Enter choice: ").strip()

        if users_pick == '1' or users_pick == '2':
            break
        else:
            print_message("Please try to enter 1 or 2")


    #todo: refactor, make more simple
    #if new game, create instance and get the random team form
    if users_pick == '1':
        new_game = Tournament()
        type = new_game.get_type()

        if type == 'Soccer':
            #get all inputs from user
            new_game.get_tournament_name()
            new_game.get_total_players()
            new_game.get_rounds()
            new_game.set_players_name()
            encryption = input("You want password protection [y/N] ").lower()
            if encryption == 'y':
                new_game.get_password()
            form = new_game.get_form()

            #if form returns an emptylist, user doesn't want fixed teams
            if form == []:
                fixed = False
            else:
                fixed = True

            total_games = int(new_game.__total_games_per_round__())*int(new_game.total_rounds)
            game_counter = new_game.game_counter

            if fixed:
                id = database.create_new_tournament(new_game.name, new_game.total_players,
                new_game.total_rounds, new_game.password, new_game.players_list, fixed, new_game.get_random_teams())
                database.add_to_sport_table(type, database.get_newest_id())
            else:
                id = database.create_new_tournament(new_game.name, new_game.total_players,
                new_game.total_rounds, new_game.password, new_game.players_list, fixed)
                database.add_to_sport_table(type, database.get_newest_id())

            fixtures = Fixtures()
            the_fixtures = fixtures.generate_fixture_list(new_game.players_list)
            database.insert_fixtures(the_fixtures, id)
            fixt_dixt = fixtures.insert_fixture_into_dict(the_fixtures)
            new_game.fixtures = fixt_dixt
            fixtures.show_fixtures()


    elif users_pick == '2':
        print_message("Reading from database ...")
        time.sleep(2)
        if database.database_is_not_empty():
            freeze_screen(2, "No leagues in the database")
            main()
        else:
            print_message("Available leagues:")
            database.print_available_leagues()

        while True:
            id = input("Enter the ID for the league you want to play? ")
            if database.get_tournament_by_id(id):
                name, players, rounds, game_counter = database.get_tournament_by_id(id)
                type = database.get_type(id)
                print("LeagueName:", name, "\nTotal Players: ", players, "\nTotal Rounds: ", rounds)
                players_dict = database.get_players_data(id, players)
                break


        #password protection
        while True:
            #todo: implement if user want password protection
            if database.is_password_protected(id):
                password = input("Enter password: ")

                if database.validate_password(id, password) is True:
                    freeze_screen(2, "Collecting data from database ...")
                    new_game = Tournament(id, type, name, rounds, players, game_counter, True)
                    new_game.set_players_name(players_dict)

                    print(LINES)
                    print_message(f"WELCOME BACK TO {new_game.name}")
                    print(LINES)
                    total_games = int(new_game.__total_games_per_round__()) * int(new_game.total_rounds)
                    fixtures = Fixtures(id)
                    fixtures.show_fixtures()

                    break
                else:
                    print_message("Incorrect password! Try again!")
            else:
                new_game = Tournament(id, type, name, rounds, players, game_counter, False)
                new_game.set_players_name(players_dict)
                print(LINES)
                print_message(f"WELCOME BACK TO {new_game.name}")
                print(LINES)
                total_games = int(new_game.__total_games_per_round__()) * int(new_game.total_rounds)
                fixtures = Fixtures(id)
                fixtures.show_fixtures()
                break

    else:
        exit("You don´t deserve us")

    while game_counter < total_games:
        new_game.game_counter += 1
        print(option.show_options())
        the_option = option.get_option()
        if validate.validate_limit(the_option, 1, 4) or the_option == "":
            if the_option == '':
                # game_number = game_counter%int(new_game.__total_games_per_round__())
                print(LINES)
                # home, away = new_game.play_next_game(game_counter)

                #hérna þarf að skila instanci í home and away
                print("NEXT GAME\n")
                home, away = new_game.play_next_game()
                print("\n", LINES)

                #this works when starting a game but not when starting an old game
                # if isinstance(random_team, str) and random_team in 'Yy':
                #     print(new_game.get_one_fixture() + "\n")


                while True:

                    score = input("Enter results, two integers with space between: ")
                    if validate.validate_score_input(score):
                        score = score.split()
                        a_game = Game(score[0], score[1], home, away)

                        #fæ villu hér því str object á ekki play_game sem er inní handle scores
                        #self.away_team er str object
                        a_game.handle_scores()
                        game_counter += 1

                        #database update scores
                        #database update fixtures
                        database.update_played_games_in_tournament_by_id(id, game_counter)

                        for i in new_game.players_list:
                            database.update_players_attributes(i.id, i.points, i.scored_goals, i.conceded_goals, i.played_games)
                        break

            elif the_option == '1':
                print(LINES)
                print(f"           ~~~~~ {new_game.name} ~~~~~")
                print(f'\nYou are playing {new_game.total_rounds} rounds of the following games')
                print(LINES)

                #todo: print only unplayed games or games with scores
                fixtures.show_fixtures()
                print(LINES)
                freeze_screen(2)


            elif the_option == '2':
                print(new_game)
                freeze_screen(2)

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
                    freeze_screen(2, "NOT AN OPTION")

            elif the_option == '4':
                print("Writing out data...")
                time.sleep(2)
                print("All set! See you soon!")
                exit()

    # the end of the loop, it shows the league standings
    # print(new_game)

main()




