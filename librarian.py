# librarian.py

from person import Person
from library import Library

class Librarian(Person):
    def __init__(self, name, surname, librarian_id):
        super().__init__(name, surname, librarian_id)
    
    def add_book(self, library, book):
        library.add_book(book)
    
    def remove_book(self, library, book):
        library.remove_book(book)
    
    def add_patron(self, library, patron):
        library.add_patron(patron)
    
    def remove_patron(self, library, patron):
        library.remove_patron(patron)
    
    def __str__(self):
        return f"Librarian(Name: {self.name} {self.surname}, ID: {self.person_id})"
