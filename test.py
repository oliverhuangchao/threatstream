import psycopg2

try:
    conn = psycopg2.connect("dbname='exampledb' user='dbuser' host='localhost' password='hc'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
cur.execute("SELECT * from second")
rows = cur.fetchall()
#print "\nShow me the databases:\n"
print rows
