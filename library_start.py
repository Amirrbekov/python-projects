from library import *

print("""********************
      
Welcome to the Library


Actions:
    
    
1. Show Books

2. Books Asks

3. Insert a book

4. Delete a book

Press q button if you want to exit
      
********************""")

library = Library()

while True:
    
    action = input("What you want to do: ")
    
    if action == 'q':
        
        print("Program is quiting...")
        print("Quited.")
        break
    
    elif action == '1':
        
        library.show_books()
    
    elif action == '2':
        
        name = input("Book name: ")
        
        print("Waiting...")
        
        library.book_ask(name)
    
    elif action == '3':
        
        name = input("Book Name: ")
        author = input("Author Name: ")
        place = input("Book publishing place: ")
        genre = input("Book Genre: ")
        page = int(input("Book Page: "))
        
        new_book = Book(name, author, place, genre, page)
        
        print("Book inserting...")
        
        time.sleep(2)
        
        library.insert_book(new_book)
        
        print("Book inserted.")
    
    elif action == '4':
        
        name = input("Book Name: ")
        
        answer = input("Really ? (y/n)")
        
        if answer=="y":
            print("Book deleting...")
            time.sleep(2)
            library.buy_book(name)
            print("Book deleted.")
    
    else:
        
        print("Wrong action.")