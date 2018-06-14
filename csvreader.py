import csv

rawdata = 'name,age\nDan,33\nBob,19\nSheri,42'
myreader = csv.reader(rawdata.splitlines())
for row in myreader:
    print(row[0], row[1])