# print all the books in the mysql database

#supoost the following table define for Books and Authors
# #Books
# isbn :primary key
# name 
# publisher
# year

# # Author:
# isbn: primary key
# name: primary key
# rank 

# It seems that Borrower and Borrowing are not used here. We just want to show all the books and its author in the database

# how to run?
# 1. install the mysql on you system
# 2. fill the the information in the following
import mysql.connector as mysqlco

# user information
user="root"
password="hc"
host='127.0.0.1'
database="threatstream"

class Book:
    def __init__(self,isbn,name,publisher,year):
        self.isbn = isbn
        self.name = name
        self.publisher = publisher
        self.year = year
        self.author_list = []
    def show_detail(self):
        print self.name
        if self.author_list:
            for each in self.author_list:
                print "   %s" % each.name
        else:
            print "Warning: do not find book titled %s in author database" % self.name
        print "%s, %d" % (self.publisher,self.year)
        print "----------"

class Author:
    def __init__(self,isbn,name,rank):
        self.isbn = isbn
        self.name = name
        self.rank = rank

def return_all_books(Connection):
    cursor = Connection.cursor()
    query = "select isbn,name,publisher,year from Books"
    try :
        cursor.execute(query)
    except mysqlco.Error as err:
        print err
        return []
    book_list = []
    book_list = map(lambda x: Book(x[0],x[1],x[2],x[3]),cursor)
    if not book_list:
        print "no books selects"
    return book_list
  

def return_author_list(Connection,book):
    cursor = Connection.cursor()
    query = "select isbn,name,rank from Author where isbn = %d" % book.isbn
    try:
        cursor.execute(query)
    except mysqlco.Error as err:
        print err
        return
    book.author_list = map(lambda x: Author(x[0],x[1],x[2]), cursor)
    if book.author_list:
        book.author_list.sort(key=lambda x:x.rank)

        
def print_books(book_list):
    for book in book_list:
        book.show_detail()

def show_books(cnx):
    book_list = return_all_books(cnx)
    if book_list:
        for book in book_list:
            return_author_list(cnx,book)
        print_books(book_list)



if __name__ == "__main__":    
    try:
        cnx = mysqlco.MySQLConnection(user=user, password=password, host=host, database=database)
        show_books(cnx)
        cnx.close()
    except mysqlco.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)