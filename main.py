# main.py

from person import Person

# Create a new person instance
person1 = Person("Bektursun", "Emlbekov", 34573 )
person2 = Person("Emirlan", "Tadjibaev", 34577)

# Print the person instances
print(person1)
print(person2)




from patron import Patron

# Create a new patron instance
patron1 = Patron("Bektursun", "Emlbekov", 34573)
patron2 = Patron("Emirlan", "Tadjibaev", 34577)

# Borrow books
patron1.borrow_book("1984 by George Orwell")
patron2.borrow_book("To Kill a Mockingbird by Harper Lee")

# Return a book
patron1.return_book("1984 by George Orwell")

# Print the patron instances
print(patron1)
print(patron2)



from librarian import Librarian
from library import Library
from patron import Patron

# Create a new library instance
library = Library("Central Library")

# Create a new librarian instance
librarian = Librarian("Bektursun", "Emlbekov", 34573)

# Create a new patron instance
patron = Patron("Emirlan", "Tadjibaev", 34577)

# Add books to the library
librarian.add_book(library, "1984 by George Orwell")
librarian.add_book(library, "To Kill a Mockingbird by Harper Lee")

# Add patron to the library
librarian.add_patron(library, patron)

# Print the library's books and patrons
print("Books in the library:", library.books)
print("Patrons in the library:", [str(p) for p in library.patrons])

# Remove a book from the library
librarian.remove_book(library, "1984 by George Orwell")

# Remove a patron from the library
librarian.remove_patron(library, patron)

# Print the library's books and patrons after removal
print("Books in the library after removal:", library.books)
print("Patrons in the library after removal:", [str(p) for p in library.patrons])