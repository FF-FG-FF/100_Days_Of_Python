#creates a class called book, to store the title,author, and the boolean availability
class Book:
    def __init__(self, book_title, author):
        self.book_title = book_title
        self.author = author
        self.is_available = True

# checks if the book is available, if its there it changes the value to 'False' and prints the statement
# if its not there / the value is 'False' it will print the book is unavailable
    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"The book '{self.book_title}' by {self.author} has been borrowed.")
        else:
            print(f"The book '{self.book_title}' by {self.author} is currently unavailable.")

# checks if the book is not available, if its not there it will change the value to true and print the statement
# if it is available or value is TRUE , it will print the book is already available
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"The book '{self.book_title}' by {self.author}' has been returned.")
        else:
            print(f"The book '{self.book_title}' by {self.author}' is already available.")


# Creating objects/instances of the Book class
book1 = Book("Harry Potter", "JK Rowling") #call the class , to store info
book2 = Book("Diary Of A Wimpy Kid", "Jeff Kinney")

# Borrowing and returning books
book1.borrow()
book1.borrow()
book2.borrow()
book2.return_book()
book1.return_book()
book1.return_book()

