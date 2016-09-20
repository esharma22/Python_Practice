#class film
from Media import Media

class Film(Media):
    """docstring for Film"""
    #constructor
    def __init__(self, call_number, title, subjects, director, notes, year):
        Media.__init__(self, call_number, title, subjects, notes)
        self.director = director
        self.year = year
    #end of constructor

    #display function
    def display(self):
        print("---------FILM--------")
        print("Call Number: " + self.call_number)
        print("Title: " + self.title)
        print("Subject: " + self.subjects)
        print("Director: " + self.director)
        print("Notes: " + self.notes)
        print("Year: " + self.year)
    #end of function

    #Function to search book using fiels discription, notes, year,
    def compare_other(self, value):
        if(self.director.find(value)):
            return True
        elif(self.notes.find(value)):
            return True
        elif(self.year.find(value)):
            return True
        else:
            return False
    #end of function

#end of class
