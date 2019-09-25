import mysql.connector
from mysql.connector import Error
from validation import Validation

class DatabaseSearcher:
    def __init__(self,):
        self.validation = Validation()
        self.connect()

    def connect(self):

        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                 database='tournament',
                                                 user='root',
                                                 password='atli2369')
            self.curs = self.connection.cursor()
        except Error as e:
            print("Error reading data from MySQL table", e)

    def get_tournament_by_id(self, ID=int):

        if self.validation.validate_integer(ID):
            ID = str(ID)
            query = "select * from tournament where id = " + ID + ";"
            self.curs.execute(query)
            records = self.curs.fetchall()

            try:
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

        # password = records[0][4]
        # return records

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
        # print(records)
        namelist = []

        for i,v in enumerate(records):
            namelist.append(records[i][0])

        return namelist

    def print_available_leagues(self):
        query = "select * from tournament"
        self.curs.execute(query)
        records = self.curs.fetchall()
        # print(records)

        for i, v in enumerate(records):
            print("ID: ", records[i][0])
            print("Tournament: ", records[i][1])
            print("Players: ", records[i][2], "\n")


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
