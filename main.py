from tournament import Tournament
# from options import Options
from validation import *
from mysqldata import DatabaseSearcher
import time
from game import Game
from fixtures import Fixtures
from team import Team

#new game
#todo: implement some stats
#todo: implement generic code to add type of sports with different score rules
#todo: when tournament finished, print a pretty WINNER and offer to play a new game and delete from database

#old game
#todo: when starting an old game, the table doesn´t work the second time. Definitely something in mysqldata!


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

    while True:
        user_input = input(input_text).strip()
        print()
        if user_input in options:
            return user_input
        else:
            print("Please try again!")

def main():
    # initialize instances and print intro.
    #todo: make sure you only print intro (def initalize) once
    database = DatabaseSearcher()
    validate = Validation()
    option = Options()
    initialize()

    #first menu
    print_message("[1] Play a new game\n[2] Continue with a league")

    #get user input from first menu above
    users_pick = get_inputs("Enter choice: ", ['1', '2'])

    # starting new tournament
    if users_pick == '1':
        #create new instance of a tournament, using the database instance
        new_game = Tournament(database=database, new=True)

        #the type of sport to have the option to scale the software
        while True:
            type = new_game.get_type()
            if type in ['Soccer', 'UFC', 'Darts']:
                break
            else:
                print("Stay focused")

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
            tournament_id = database.create_new_tournament(name=new_game.name,
                                                total_players=new_game.total_players,
                                                total_rounds=new_game.total_rounds,
                                                password=new_game.password,
                                                namelist=new_game.players_list,
                                                fixed=fixed,
                                                rand_list=form)

            database.add_to_sport_table(type, database.get_newest_id('Tournament'))

            #todo: refactor this part

            #new instance of fixtures
            fixtures = Fixtures(database)

            #generate fixtures as list and then adding to dictionary
            the_fixtures = fixtures.generate_fixture_list(new_game.players_list, new_game.total_rounds)
            fixt_dixt = fixtures.insert_fixture_into_dict(the_fixtures)

            #insert into database
            database.insert_fixtures(the_fixtures, tournament_id)

            #assigning the fixt_dixt to the new_game instance self.fixtures
            new_game.fixtures = fixt_dixt

            #showing all fixtures before tournament starts
            fixtures.show_fixtures(tournament_id=database.get_newest_id('Tournament'))

        elif type == 'UFC':
            freeze_screen(1, "UFC not ready. Application closing ...")
            quit()

        elif type == 'Darts':
            freeze_screen(1, "Darts not ready. Application closing ...")
            quit()

    #below is playing a league that already exists
    elif users_pick == '2':
        freeze_screen(2, "Reading from database ...")
        if database.is_not_empty():
            freeze_screen(2, "No leagues in the database")
            main()
        else:
            print_message("Available leagues:")
            database.print_available_leagues()

        #picking tournament tournament_id from a list
        while True:
            tournament_id = input("Enter the ID for the league you want to play? ")
            if database.get_tournament_by_id(tournament_id):
                name, players, rounds, game_counter = database.get_tournament_by_id(tournament_id)
                type = database.get_type(tournament_id)
                print("LeagueName:", name, "\nTotal Players: ", players, "\nTotal Rounds: ", rounds)
                players_dict = database.get_players_data(tournament_id=tournament_id)
                print(players_dict, "þetta er elísa")
                break

        #password protection
        while True:
            if database.is_password_protected(tournament_id=tournament_id) is True:
                password = input("Enter password: ")
                if database.validate_password(id=tournament_id,password=password) is True:
                    freeze_screen(2, "Collecting data from database ...")
                    break
                else:
                    print_message("Incorrect password! Try again!")

            else:
                print("\n\nMaybe you should use a password next time.\n ")
                break


        #create players list

        #setting up new instance of tournament as new.game
        new_game = Tournament(database=database,
                              tournament_id=tournament_id,
                              type=type,
                              name=name,
                              rounds=rounds,
                              players=players,
                              game_counter=game_counter,
                              players_list=None,
                              new=False)

        #inserting into team instances
        new_game.set_players_name(players_dict=players_dict)


        print(LINES)
        print_message(f"WELCOME BACK TO {new_game.name}")
        print(LINES)

        #getting the total games for the play loop
        total_games = new_game.total_games

        # new instance of fixtures
        fixtures = Fixtures(database=database,
                            tournament_id=new_game.tournament_id)


        #generate one list of fixtures from team instances in players list and excludes the day off
        the_fixtures = fixtures.generate_fixture_list(new_game.players_list, new_game.total_rounds)
        fixt_dixt = fixtures.insert_fixture_into_dict(the_fixtures, tournament_id=tournament_id)

        new_game.fixtures = fixt_dixt

        print(new_game.fixtures)

        fixtures.show_fixtures(tournament_id=tournament_id)

    else:
        exit("You don´t deserve us")

    #playing a game with new_game as instance of Tournament
    while game_counter < total_games:
        print(option.show())
        the_option = option.get()
        if validate.limit(the_option, 1, 4) or the_option == "":
            if the_option == '':
                print(LINES)
                home, away = new_game.play_next_game(tournament_id=new_game.tournament_id,
                                                     game_counter=new_game.game_counter)
                print("\n", LINES)

                # getting the score for the game
                while True:
                    score = input("Enter results, two integers with space between: ")
                    if validate.scores(score):
                        score = score.split()
                        a_game = Game(game_counter, score[0], score[1], home, away)
                        score_list = [int(a_game.home_score), int(a_game.away_score)]


                        fixtures.insert_score_to_fixture(score_list, game_counter)
                        database.update_fixture_table(game_id=a_game.id,
                                                      tournament_id=tournament_id,
                                                      home_id=home.id,
                                                      away_id=away.id,
                                                      scores=score_list)
                        a_game.handle_scores()
                        #updating fixtures
                        database.updated_played(tournament_id=tournament_id,
                                                game_id=game_counter)
                        game_counter += 1
                        new_game.game_counter += 1
                        database.update_played_games_in_tournament_by_id(tournament_id=int(new_game.tournament_id)+1,
                                                                         played_games=game_counter)


                        database.update_players_attributes(tournament_id=tournament_id,
                                                           team_id=home.id,
                                                           points=home.points,
                                                           scored=home.scored_goals,
                                                           conceded=home.conceded_goals,
                                                           played=home.played_games)

                        database.update_players_attributes(tournament_id= tournament_id,
                                                           team_id=away.id,
                                                           points=away.points,
                                                           scored=away.scored_goals,
                                                           conceded=away.conceded_goals,
                                                           played=away.played_games)
                        break

            elif the_option == '1':
                print(LINES)
                print(f"           ~~~~~ {new_game.name} ~~~~~")
                print(f'\nYou are playing {new_game.total_rounds} rounds of the following games')
                print(LINES)

                #todo: print only unplayed games or games with scores
                fixtures.show_fixtures(tournament_id=tournament_id)
                print(LINES)
                freeze_screen(2)


            elif the_option == '2':
                print(new_game)
                freeze_screen(2)

            elif the_option == '3':
                print(option.show_stats())
                stat_option = input("Pick your stat: ")

                if stat_option == '1':
                    print(new_game.get_biggest_win())

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




