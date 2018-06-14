import psycopg2

conn = psycopg2.connect("host=52.66.53.95 dbname=postgres user=postgres password=postgres")
cur = conn.cursor()
with open('SampleCSVFile_2kb.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, users="Muhammed MacIntyre", sep=',')

conn.commit()