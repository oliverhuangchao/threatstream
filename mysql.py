import mysql.connector as mysqlco
cnx = mysqlco.MySQLConnection(user="root", password="hc", host='127.0.0.1', database="threatstream")

#cnx = mysql.connector.connect(user='scott', database='employees')
cursor = cnx.cursor()

query = ("select * from Books")

#hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(1999, 12, 31)

#cursor.execute(query, (hire_start, hire_end))

cursor.execute(query)

print cursor
for (isbn, name, publisher, year) in cursor:
	print isbn
	print isbn
	print publisher
	print year  
#print("{}, {} was hired on {:%d %b %Y}".format(
  #  last_name, first_name, hire_date))

#cursor.close()
cnx.close()