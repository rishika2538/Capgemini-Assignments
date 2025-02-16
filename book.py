class Book:
    def __init__(self, title, author, isbn, copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.copies=copies 

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available Copies: {self.copies}")

    def borrow_book(self):
        if self.copies>0:
            self.copies-=1
            print(f"You have borrowed '{self.title}'. Copies left: {self.copies}")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        self.copies += 1
        print(f"Copies available: {self.copies}")

book1 = Book("The Alchemist", "Paulo Coelho", "978-0061122415", 5)
book1.display_info()
book1.borrow_book()
book1.return_book()
