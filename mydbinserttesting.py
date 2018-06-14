conn = psycopg2.connect(
    host='mydb.mydatabase.us-west-2.redshift.amazonaws.com',
    user='user',
    port=5439,
    password='password',
    dbname='example_db')

cur = conn.cursor()

cur.execute(statement)
conn.commit()

sql = """copy stack_overflow_survey_data from 's3://an-example-bucket/survey_data.csv'
    access_key_id '<access_key_id>'
    secret_access_key '<secret_access_key>'
    region 'us-west-1'
    ignoreheader 1
    null as 'NA'
    removequotes
    delimiter ',';"""
cur.execute(sql)
conn.commit()
