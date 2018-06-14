import csv

with open('iinclude.in_facebook_statuses.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)

csvFile.close()