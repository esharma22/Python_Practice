#Periodic class
from Media import Media

class Periodic(Media):
    """docstring for Periodic"""
    #constructor
    def __init__(self, call_number, title, subjects, author, description, publisher, publishing_history, series, notes, related_titles, other_titles, govt_number):
        Media.__init__(self, call_number, title, subjects, notes)
        self.author = author
        self.description = description
        self.publisher = publisher
        self.publishing_history = publishing_history
        self.series = series
        self.related_titles = related_titles
        self.other_titles = other_titles
        self.govt_number = govt_number
    #end of constructor

    #display function
    def display(self):
        print( "------PERIODIC------")
        print("Call Number       : "+ self.call_number )
        print("Title             : "+ self.title )
        print("Subjects          : "+ self.subjects )
        print("Author            : "+ self.author )
        print("Description       : "+ self.description )
        print("Publisher         : "+ self.publisher )
        print("Publishing History: "+ self.publishing_history)
        print("Series            : "+ self.series )
        print("Notes             : "+ self.notes )
        print("Related Titles    : "+ self.related_titles )
        print("Other Titles      : "+ self.other_titles )
        print("Govt. Doc. Number : "+ self.govt_number )
    #end of function

    #Function to search book using fiels discription, notes, year,
    def compare_other(self, value):
        if(self.description.find(value)):
            return True
        elif(self.notes.find(value)):
            return True
        elif(self.series.find(value)):
            return True
        else:
            return False
    #end of function

#end of class
