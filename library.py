class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}")

class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print("Book not found.")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None  
    
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("\nLibrary Collection:")
        for book in self.books:
            book.display_info()

library = Library()
book1 = Book("john", "Paulo ", "9785", 5)
book2 = Book("Till", "Lee", "97834", 3)

library.add_book(book1)
library.add_book(book2)

library.display_books()

isbn_to_find = "9785"
found_book = library.find_book(isbn_to_find)
if found_book:
    print("\nBook Found:")
    found_book.display_info()
else:
    print("\nBook not found.")

library.remove_book("9785")
library.display_books()