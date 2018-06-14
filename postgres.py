import psycopg2
import sys

con = None
#conn = psycopg2.connect("host=52.66.53.95 dbname=postgres user=postgres password=postgres")
try:
    con = psycopg2.connect("host='52.66.53.95' dbname='postgres' user='postgres' password='postgres'")
    cur = con.cursor()
    cur.execute("SELECT * FROM facebook")

    while True:
        row = cur.fetchone()

        if row == None:
            break

        print("Product: " + row[1] + "\t\tPrice: " + str(row[2]))

except psycopg2.DatabaseError, e:
    if con:
        con.rollback()

    print 'Error %s' % e
    sys.exit(1)

finally:
    if con:
        con.close()