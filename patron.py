# patron.py # patron.py # patron.py 
# patron.py # patron.py # patron.py  
# patron.py # patron.py # patron.py 
from person import Person

class Patron(Person):
    def __init__(self, name, surname, patron_id):
        super().__init__(name, surname, patron_id)
        self.borrowed_books = []
    
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self.name} && {self.surname} borrowed {book}")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} && {self.surname} returned {book}")
        else:
            print(f"{self.name} && {self.surname} does not have {book}")
    
    def __str__(self):
        return f"Patron(Name: {self.name}, {self.surname}, ID: {self.person_id}, Borrowed Books: {self.borrowed_books})"
