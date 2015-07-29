# here is 


# return all the books
class Book:
    def __init__(self,isbn,name,publisher,year):
        self.isbn = isbn
        self.name = name
        self.publisher = publisher
        self.year = year
        self.authorlist = []





def return_all_books(Connection):
    Connection.runquery("select * from Books")
    book_list = map(lambda x: Book(x[0],x[1],x[2],x[3]))
    return book_list



def return_author_list(Connection,book_list):
    for each_book in book_list:
        query = "select * from Authors where isbn = %d" % each_book.isbn
        result = Connection.runquery(query)
        

