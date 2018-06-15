#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

try:
    con = psycopg2.connect("host='52.66.53.95' dbname='postgres' user='postgres' password='postgres'")
    cur = con.cursor()
    cur.execute("CREATE TABLE myfacebook2(status_id VARCHAR(100000), status_message VARCHAR(100000), status_type VARCHAR(10000),status_link VARCHAR(1000),status_published VARCHAR(1000),num_reactions INTEGER,num_comments INTEGER,num_shares INTEGER,num_likes INTEGER, num_loves INTEGER, num_wows INTEGER, num_hahas INTEGER,num_sads INTEGER,num_angrys INTEGER,num_special INTEGER)")
    #cur.execute("INSERT INTO Products VALUES(1,'Milk',5)")
    #cur.execute("INSERT INTO Products VALUES(2,'Sugar',7)")
    #cur.execute("INSERT INTO Products VALUES(3,'Coffee',3)")
    #cur.execute("INSERT INTO Products VALUES(4,'Bread',5)")
    #cur.execute("INSERT INTO Products VALUES(5,'Oranges',3)")
    con.commit()
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()

    print 'Error %s' % e
    sys.exit(1)

finally:
    if con:
        con.close()