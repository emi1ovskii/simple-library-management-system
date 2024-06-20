# library.py

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' not found in the library.")

    def add_patron(self, patron):
        self.patrons.append(patron)
        print(f"Patron '{patron.name}' added to the library.")

    def remove_patron(self, patron):
        if patron in self.patrons:
            self.patrons.remove(patron)
            print(f"Patron '{patron.name}' removed from the library.")
        else:
            print(f"Patron '{patron.name}' not found in the library.")
