import mysql.connector
from mysql.connector import Error
# from team import *

from validation import Validation

#todo: add fixturetable to database, how do we keep track on scores? Scorestable?


class DatabaseSearcher:
    def __init__(self):
        self.validation = Validation()
        self.connect()

    def connect(self):

        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      database='tournament',
                                                      user='root',
                                                      password='Klemmisinn?') #atli2369 Klemmisinn
            self.curs = self.connection.cursor(buffered=True)
        except Error as e:
            print("Error reading data from MySQL table", e)

    def get_tournament_by_id(self, ID=int):

        if self.validation.validate_integer(ID):
            ID = str(ID)
            query = "select * from tournament where id = " + ID + ";"
            self.curs.execute(query)
            records = self.curs.fetchall()

            try:
                # type = records[0][0]
                name = records[0][1]
                players = records[0][2]
                rounds = records[0][3]
                played_games = records[0][5]
                return name, players, rounds, played_games

            except IndexError:
                print(f"\nTournament with ID {ID} doesn´t exists.\n")
                return False
        else:
            return False

    def validate_password(self, id, password):

        ID = str(id)
        query = "select * from tournament where id = " + ID + ";"
        self.curs.execute(query)
        records = self.curs.fetchall()
        return password == records[0][4]

    def get_players_data(self, id, total_players):
        print("Total Players:", total_players)

        ID = str(id)
        query = "select * from team where tournament_id = " + ID + ";"
        self.curs.execute(query)
        records = self.curs.fetchall()
        namedict = {}

        for i,attrib in enumerate(records):
            name = records[i][0]
            namedict[name] = []
            namedict[name].append(attrib[1:])
        return namedict

    def print_available_leagues(self):
        query = "select * from tournament"
        self.curs.execute(query)
        records = self.curs.fetchall()

        for i, v in enumerate(records):
            print("ID: ", records[i][0])
            print("Tournament: ", records[i][1])
            print("Players: ", records[i][2], "\n")

    def update_played_games_in_tournament_by_id(self, ID=int, played_games=int):

        ID = str(ID)
        played = str(played_games)

        query = "UPDATE tournament " + "SET played_games = " + played + " WHERE id = " + ID + ";"

        self.curs.execute(query)
        self.connection.commit()

    def create_new_tournament(self,name:str,total_players:str,total_rounds:str, password:str, namelist:list, fixed:bool, rand_list=None):

        total_players = str(total_players)
        rounds = str(total_rounds)
        password = str(password)
        name = str(name)


        sql = "INSERT INTO tournament (name, total_players, total_rounds, password, played_games, fixed_teams) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"

        val = (name, total_players, rounds, password, 0, fixed)

        self.curs.execute(sql, val)
        self.connection.commit()
        tournament_id = self.get_newest_id()

        if rand_list:
            self.__add_players_to_tournament(namelist, tournament_id, rand_list)
        else:
            self.__add_players_to_tournament(namelist, tournament_id)

        return tournament_id

    def __add_players_to_tournament(self, namelist, tournament_id, team=False):

        points = 0
        scored = 0
        conceded = 0
        played = 0
        tournament_id = str(tournament_id)

        sql = "INSERT INTO team (name, points, scored_goals, conceded_goals, played_games, tournament_id, assigned_team) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s)"

        if team:
            for index, value in enumerate(namelist):
                val = (str(value), points, scored, conceded, played, tournament_id, team[index])
                self.curs.execute(sql, val)
                self.connection.commit()
        else:
            for index, value in enumerate(namelist):
                val = (str(value), points, scored, conceded, played, tournament_id, False)
                self.curs.execute(sql, val)
                self.connection.commit()

    def add_to_sport_table(self, sportname, tournament_id):
        #todo: insert the sport type to the database
        sportname = str(sportname)
        tournament_id = str(tournament_id)

        sql = "INSERT INTO sports (Sportname, tournament_id) " \
              "VALUES (%s, %s)"

        val = (sportname, tournament_id)

        self.curs.execute(sql, val)
        self.connection.commit()

    def get_newest_id(self):
        return_value = "SELECT id FROM tournament ORDER BY id DESC LIMIT 1;"
        self.curs.execute(return_value)
        records = self.curs.fetchone()
        return records[0]

    def find_next_player_id(self):
        try:
            return_value = "SELECT id FROM team ORDER BY id DESC LIMIT 1;"
            self.curs.execute(return_value)
            records = self.curs.fetchone()
            return int(records[0])+1
        except:
            return False

    def database_is_not_empty(self):
        try:
            return_value = "SELECT * from tournament;"
            self.curs.execute(return_value)
            records = self.curs.fetchone()
            if len(records) == 0:
                return False
        except:
            return True

    def get_fixtures(self, id):
        '''Should return a dict of fixtures {1: [liverpool, Arsenal], 2 [Chelsea ... ] '''
        if self.validation.validate_integer(id):
            ID = str(id)
            query = "select * from fixtures where tournament_id = " + ID + ";"
            self.curs.execute(query)
            records = self.curs.fetchall()

            return_dict = {}

            for value in records:
                key = value[0]
                hometeam = value[3]
                awayteam = value[4]
                played = value[2]
                # print("Game number:", value[0], end=" ")
                # print("played:", value[2], end=" ")
                # print("HomeTeam:", value[3], end=" VS ")
                # print("AwayTeam:", value[4], end=" ")
                # print()
                return_dict[key] = [(hometeam, awayteam), played]

            # print(return_dict)


            return return_dict

        #     try:
        #         # type = records[0][0]
        #         name = records[0][1]
        #         players = records[0][2]
        #         rounds = records[0][3]
        #         played_games = records[0][5]
        #         return name, players, rounds, played_games
        #
        #     except IndexError:
        #         print(f"\nTournament with ID {ID} doesn´t exists.\n")
        #         return False
        # else:
        #     return False
        # pass

    def updated_played(self, tournament_id, game_id):
        game_id = str(game_id)
        t_id = str(tournament_id)
        played = str(1)

        query = "UPDATE fixtures " + \
                "SET " \
                "played = " + played + \
                " WHERE game_id = " + game_id +\
                " AND tournament_id = " + t_id + ";"

        self.curs.execute(query)
        self.connection.commit()


    def is_played(self, tournament_id, game_id):
        game_id = str(game_id)
        t_id = str(tournament_id)

        query = "SELECT played from fixtures where tournament_id = " + t_id + \
                " AND game_id = " + game_id + ";"


        self.curs.execute(query)
        records = self.curs.fetchone()
        # print(records, "þetta eru records")
        # print(records[0], "þetta eru records[0]")
        # print(type(records[0]), "týpan af records[0]")
        if records[0] == 0:
            return False

        return True

        #     return False
        # except:
        #     return False
        # if records:
        #
        # print(records[0], "ÞETTA ERU RECORDS")
        #
        # return records[0]


    def update_players_attributes(self, id, points, scored, conceded, played):
        id = str(id)
        points = str(points)
        scored = str(scored)
        conceded = str(conceded)
        played = str(played)

        query = "UPDATE team " +\
                "SET " \
                "played_games = " + played +\
                ", points = " + points +\
                ", scored_goals = " + scored +\
                ", conceded_goals = " + conceded +\
                " WHERE id = " + id + ";"

        self.curs.execute(query)
        self.connection.commit()




        # def update_teams_attributes_in_tournament_by_id(self, ID=int, played_games=int):
        #
        #     if self.validation.validate_integer(ID):
        #         ID = str(ID)
        #         played = str(played_games)
        #
        #         query = "UPDATE tournament " + "SET played_games = " + played + " WHERE id = " + ID + ";"
        #
        #         self.curs.execute(query)
        #         self.connection.commit()

        #
        # try:
        #     id = '1'
        #
        #     connection = mysql.connector.connect(host='localhost',
        #                                          database='tournament',
        #                                          user='root',
        #                                          password='atli2369')
        #
        #     sql_select_Query = "select * from tournament where id = " + id + ";"
        #     cursor = connection.cursor()
        #     cursor.execute(sql_select_Query)
        #     records = cursor.fetchall()
        #     print(records)
        #     print("Total number of rows in team is: ", cursor.rowcount)
        #
        #     # print("\nPrinting each laptop record")
        #     # for row in records:
        #     #     print("Id = ", row[0], )
        #     #     print("Name = ", row[1])
        #     #     print("Price  = ", row[2])
        #     #     print("Purchase date  = ", row[3], "\n")
        #
        # except Error as e:
        #     print("Error reading data from MySQL table", e)
        # # finally:
        # #     if (connection.is_connected()):
        # #         connection.close()
        # #         cursor.close()
        # #         print("MySQL connection is closed")
        #
        #
        # def get_id(self, ID):
        #     pass

        # id = 1
        # Database = DatabaseSearcher(id, 'john')
        # name, players, rounds = Database.get_tournament_by_id(1)
        #
        #
        # # password = tournamentdata[0][4]
        # #testpassword
        # password = '1234'
        #
        # if Database.validate_password(id, password):
        #     print("Password matches!")
        # else:
        #     print("incorrect password")
        #
        #
        # Database.get_players_data(id, players)
        #
        # Database.print_available_leagues()

    def is_password_protected(self, tournament_id):
        try:
            query = "SELECT password from tournament WHERE id = " + tournament_id + ";"
            self.curs.execute(query)
            records = self.curs.fetchone()
            if len(records) == 0:
                return False
        except:
            return True

    def insert_fixtures(self, fixture_list, tournament_id):

        game_nr = 0
        for rounds in fixture_list:
            for fixt in rounds:
                game_nr += 1
                home = fixt[0].name
                away = fixt[1].name
                # print("GAMENUMBER", game_nr, "ASDADASDASDAS")



                sql = "INSERT INTO fixtures (game_id, tournament_id, played, hometeamname, awayteamname) " \
                    "VALUES (%s, %s, %s, %s, %s)"
                val = (game_nr, tournament_id, 0, home, away)
                self.curs.execute(sql, val)
        self.connection.commit()


    def get_type(self, id):
        ID = str(id)
        query = "select sportname from sports where tournament_id = " + ID + ";"
        self.curs.execute(query)
        records = self.curs.fetchone()
        return records[0]