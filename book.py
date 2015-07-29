# here is 
import mysql.connector as mysqlco


# return all the books
class Book:
    def __init__(self,isbn,name,publisher,year):
        self.isbn = isbn
        self.name = name
        self.publisher = publisher
        self.year = year
        self.author_list = []
    def show_detail(self):
        print self.name
        for each in self.author_list:
            print each.name
        print "%s, %d" % (self.publisher,self.year)
        print "----------"

class Author:
    def __init__(self,isbn,name,rank):
        self.isbn = isbn
        self.name = name
        self.rank = rank

def return_all_books(Connection):
    cursor = Connection.cursor()
    query = ("select * from Books")
    cursor.execute(query)
    book_list = []
    book_list = map(lambda x: Book(x[0],x[1],x[2],x[3]),cursor)
    #book_list.reverse()
    #for (isbn, name, publisher, year) in cursor:
    #    book_list.append(Book(isbn, name, publisher, year))
    return book_list



def return_author_list(Connection,book):
    cursor = Connection.cursor()
    query = "select * from Author where isbn = %d" % book.isbn
    cursor.execute(query)
    book.author_list = map(lambda x: Author(x[0],x[1],x[2]), cursor)
    book.author_list.reverse()

        
def showBooks(book_list):
    for book in book_list:
        book.show_detail()




cnx = mysqlco.MySQLConnection(user="root", password="hc", host='127.0.0.1', database="threatstream")
book_list = return_all_books(cnx)
for book in book_list:
    return_author_list(cnx,book)
showBooks(book_list)
cnx.close()