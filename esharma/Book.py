from Media import Media
class Book(Media):
    """Class for Book object"""
    #class variables
    def __init__(self, call_number, title, subjects, author, description, publisher, city, year, series, notes):
        Media.__init__(self, call_number, title, subjects, notes)
        self.author = author
        self.description = description
        self.publisher = publisher
        self.city = city
        self.year = year
        self.series = series
    #end of constructor

    #Display Function
    def display(self):
        print("------BOOK------")
        print("Call Number: " + self.call_number)
        print("Title: " + self.title)
        print("Subject: " + self.subjects)
        print("Author: " + self.author)
        print("Description: " + self.description)
        print("Publisher: " + self.publisher)
        print("City: " + self.city)
        print("Year: " + self.year)
        print("Series: " + self.series)
        print("Notes: " + self.notes)
    #end of function

    #Function to search book using fiels discription, notes, year,
    def compare_other(self, value):
        if(self.description.find(value)):
            return True
        elif(self.notes.find(value)):
            return True
        elif(self.year.find(value)):
            return True
        else:
            return False
    #end of function
