import csv

with open('data.csv', 'r', encoding="utf8") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)