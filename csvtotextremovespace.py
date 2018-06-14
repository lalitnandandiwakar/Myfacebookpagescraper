import csv

csv.register_dialect('myDialect',
delimiter = ',',
skipinitialspace=True)

with open('mytestingdb.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    for raw in reader:
        print(raw)

csvFile.close()