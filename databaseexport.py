import csv
import psycopg2

conn = psycopg2.connect("host=52.66.53.95 dbname=facebook user=postgres password=postgres")
cur = conn.cursor()

with open('iinclude.in_facebook_statuses.csv', 'r') as f:
    reader = csv.reader(f)
 #   next(reader)  # Skip the header row.
    for row in reader:
        cur.execute(
            "INSERT INTO myfacebook2 VALUES (%s, %s, %s)",
            row
        )
conn.commit()