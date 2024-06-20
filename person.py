class Person:
    def __init__(self, name, surname, person_id):
        self.name = name
        self.surname = surname 
        self.person_id = person_id
    
    def __str__(self):
        return f"Person(Name: {self.name}, {self.surname} ID: {self.person_id})"
    


