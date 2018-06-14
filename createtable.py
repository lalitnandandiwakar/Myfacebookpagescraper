import psycopg2

conn = psycopg2.connect("host=52.66.53.95 dbname=postgres user=postgres password=postgres")
print "Opened database successfully"

cur = conn.cursor()
cur.execute('''CREATE TABLE facebook2
      (ID            TEXT,
      NAME           TEXT,
      AGE            TEXT);''')
print "Table created successfully"

conn.commit()
conn.close()