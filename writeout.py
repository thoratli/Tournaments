import csv
from datareader import abstract_model
from tournament import *
from team import *


class WriteOut():
    def __init__(self):
        self.data = abstract_model()


    def tournament_data(self):
        return self.data.tournaments


    def players_data(self):
        return self.data.players_data


    def build_export_data(self):
        print("Atli")
        tournament = self.tournament_data()

        print(tournament)
        players_data = self.players_data()


        for k,v in tournament.items():
            print("asda")
            print(k,v)



    row = ['Hawgs', ' Marie', ' California']

    with open('Files/tester.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        lines[0] = row

    with open('Files/tester.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


    readFile.close()
    writeFile.close()


Write = WriteOut()
Write.build_export_data()