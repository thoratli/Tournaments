import configparser
from tournament import Tournament
# from options import Options
from validation import *
from mysqldata import DatabaseSearcher
import time
from game import Game
from fixtures import Fixtures
from team import Team

#new game
#todo: we are not taking rounds into account when printing fixtures and scores with it, needs multiplication
#todo: implement some stats
#todo: implement generic code to add type of sports with different score rules
#todo: when tournament finished, print a pretty WINNER and offer to play a new game and delete from database

#old game
#todo: when read from database, showing fixtures and playing fixture doesn´t work. Instance/DB problem


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

def get_inputs(input_text, options: list):
    """Takes in the input text and the list of options
    and returns the input if valid"""
    for i in options:
        print(i)

    while True:
        user_input = input(input_text).strip()
        print()
        print(user_input)
        if user_input in options:
            return user_input
        else:
            print()

def main():
    # initialize instances and print intro.
    #todo: make sure you only print intro (def initalize) once
    config = configparser.ConfigParser()
    config.read('./config.ini')
    database = DatabaseSearcher(host=config['db']['host'],
                                user=config['db']['user'],
                                password=config['db']['password'],
                                database=config['db']['database'])
    validate = Validation()
    option = Options()
    initialize()

    #first menu
    print_message("[1] Play a new game\n[2] Continue with a league")

    #get user input from first menu above
    users_pick = get_inputs("Enter choice: ", ['1', '2'])

    if users_pick == '1':
        #create new instance of a tournament, using the database instance
        new_game = Tournament(database=database, new=True)

        #the type of sport to have the option to scale the software
        type = new_game.get_type()

        if type == 'Soccer':
            #get all inputs from user
            new_game.get_tournament_name()
            new_game.get_total_players()
            new_game.get_rounds()
            new_game.set_players_name()
            new_game.set_total_games()

            #checks if user wants password in his tournament
            encryption = get_inputs("You want password protection [y/N] ", ['y', 'Y', 'N', 'n', ""])
            if encryption.lower() == "y":
                new_game.get_password()

            # if form returns an emptylist, user doesn't want fixed teams
            # else it a a list of random teams to put in database
            form = new_game.get_form()
            if form == []:
                fixed = False
            else:
                fixed = True

            #from the instance, init total_games and game_counter variables for the playLOOP
            total_games = new_game.total_games
            game_counter = new_game.game_counter

            #database insertion, insert into tournament and insert into sport table
            id = database.create_new_tournament(name=new_game.name,
                                                total_players=new_game.total_players,
                                                total_rounds=new_game.total_rounds,
                                                password=new_game.password,
                                                namelist=new_game.players_list,
                                                fixed=fixed,
                                                rand_list=form)

            database.add_to_sport_table(type, database.get_newest_id())

            #todo: refactor this part
            fixtures = Fixtures(database)
            the_fixtures = fixtures.generate_fixture_list(new_game.players_list,new_game.total_rounds)
            database.insert_fixtures(the_fixtures, id)
            fixt_dixt = fixtures.insert_fixture_into_dict(the_fixtures)
            new_game.fixtures = fixt_dixt
            fixtures.show_fixtures(tournament_id=id)

        elif type == 'UFC':
            freeze_screen(1, "UFC not ready. Application closing ...")
            quit()

        elif type == 'Darts':
            freeze_screen(1, "Darts not ready. Application closing ...")
            quit()


    #below is playing a league that already exists
    elif users_pick == '2':
        freeze_screen(2, "Reading from database ...")
        if database.database_is_not_empty():
            freeze_screen(2, "No leagues in the database")
            main()
        else:
            print_message("Available leagues:")
            database.print_available_leagues()

        #picking tournament id from a list
        while True:
            id = input("Enter the ID for the league you want to play? ")
            if database.get_tournament_by_id(id):
                name, players, rounds, game_counter = database.get_tournament_by_id(id)
                type = database.get_type(id)
                print("LeagueName:", name, "\nTotal Players: ", players, "\nTotal Rounds: ", rounds)
                players_dict = database.get_players_data(id=id,
                                                         total_players=players)
                break

        #password protection
        while True:
            if database.is_password_protected(tournament_id=id) is True:
                password = input("Enter password: ")
                if database.validate_password(id=id,password=password) is True:
                    freeze_screen(2, "Collecting data from database ...")
                    break
                else:
                    print_message("Incorrect password! Try again!")

            else:
                print("\n\nMaybe you should use a password next time.\n ")
                break

        #setting up new instance of tournament as new.game
        new_game = Tournament(database=database,
                              id=id,type=type,
                              name=name,
                              rounds=rounds,
                              players=players,
                              game_counter=game_counter,
                              players_list=None,
                              new=False)
        new_game.set_players_name(players_dict=players_dict)

        print(LINES)
        print_message(f"WELCOME BACK TO {new_game.name}")
        print(LINES)

        #getting the total games for the play loop
        total_games = int(new_game.__total_games_per_round__()) * int(new_game.total_rounds)

        #todo: needs to fix to its working with the old instance
        fixtures = Fixtures(id)
        fixtures.show_fixtures(tournament_id=id)


    else:
        exit("You don´t deserve us")


    #playing a game with new_game as instance of Tournament
    while game_counter < total_games:
        new_game.game_counter += 1
        print(option.show())
        the_option = option.get()
        if validate.validate_limit(the_option, 1, 4) or the_option == "":
            if the_option == '':
                # game_number = game_counter%int(new_game.__total_games_per_round__())
                print(LINES)
                home, away = new_game.play_next_game(id, new_game.game_counter)
                print("\n", LINES)

                # getting the score for the game
                while True:
                    score = input("Enter results, two integers with space between: ")
                    if validate.validate_score_input(score):
                        score = score.split()
                        a_game = Game(score[0], score[1], home, away)
                        score_list = [int(a_game.home_score), int(a_game.away_score)]
                        fixtures.insert_score_to_fixture(score_list, game_counter)
                        a_game.handle_scores()
                        game_counter += 1

                        #update played games for the tournament and attributes for the players
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
                fixtures.show_fixtures(tournament_id=id)
                print(LINES)
                freeze_screen(2)


            elif the_option == '2':
                print(new_game)
                freeze_screen(2)

            elif the_option == '3':
                print(option.show_stats())
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
    print(new_game)
    print("\n\n\n", LINES)
    print("CONGRATULATIONS\n", end=" ")
    #needs some fine tuning, get the tie, tiebreakers...
    print(new_game.get_winner())

    print("\n\n", LINES)

main()




