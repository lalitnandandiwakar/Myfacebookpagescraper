import csv
import psycopg2

conn = psycopg2.connect("host=52.66.53.95 dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

with open('C:\Users\lalitnandan\PycharmProjects\myfacebookpagescraper\SampleCSVFile_2kb.csv', 'r') as f:
    reader = csv.reader(f)
 #   next(reader)  # Skip the header row.
    for row in reader:
        cur.execute(
            "INSERT INTO users VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s)",
            row
        )
conn.commit()