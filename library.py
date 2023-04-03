import sqlite3

import time

class Book():
    
    def __init__(self, name, author, place, genre, page):
        
        self.name = name
        self.author = author
        self.place = place
        self.genre = genre
        self.page = page
        
    def __str__(self):
        
        return "Book name: {}\nBook author: {}\nBook publishing place: {}\nBook genre: {}\nBook pages: {}\n".format(self.name, self.author, self.place, self.genre, self.page)
    
class Library():
    
    def __init__(self):
        
        self.create_connect()
        
    def create_connect(self):
        
        self.connect = sqlite3.connect("libarary.db")
        
        self.cursor = self.connect.cursor()
        
        request = "Create Table If not exists books (name TEXT, author TEXT, place TEXT, genre TEXT, page INT)"
        
        self.cursor.execute(request)
        
        self.connect.commit()
        
    def disconnect(self):
        
        self.connect.close()
        
    def show_books(self):
        
        request = "Select * From books"
        
        self.cursor.execute(request)
        
        books = self.cursor.fetchall()
        
        if (len(books)==0):
            
            print("There are no books in the library")
            
        else:
            
            for i in books:
                
                book = Book(i[0],i[1],i[2],i[3],i[4])
                
                print(book)
                
    def book_ask(self,name):
        
        request = "Select * From books where name = ?"
        
        self.cursor.execute(request,(name,))
        
        books = self.cursor.fetchall()
        
        if (len(books)==0):
            
            print("No such book was found")
            
        else:
            
            book = Book(books[0][0],books[0][1],books[0][2],book[0],[3],book[0][4])
            
            print(book)
            
    def insert_book(self,book):
        
        request = "Insert into books Values(?,?,?,?,?)"
        
        self.cursor.execute(request,(book.name,book.author,book.place,book.genre,book.page))
        
        self.connect.commit()
        
    def buy_book(self,name):
        
        request = "Delete From books where name = ?"
        
        self.cursor.execute(request,(name,))
        
        self.connect.commit()
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        