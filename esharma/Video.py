#Class Video
from Media import Media
class Video(Media):
    """docstring for Video"""
    #constructor
    def __init__(self, call_number, title, subjects, description, distributor, notes, series, label):
        Media.__init__(self, call_number, title, subjects, notes)
        self.description = description
        self.distributor = distributor
        self.series = series
        self.label = label
    #end of constructor

    #Display function
    def display(self):
        print("------VIDEO------")
        print("Call Number: " + self.call_number)
        print("Title: " + self.title)
        print("Subject: " + self.subjects)
        print("Description: " + self.description)
        print("Distributor: " + self.distributor)
        print("Notes: " + self.notes)
        print("Series: " + self.series)
        print("Label: " + self.label)
    #end of function

    #Function to search book using fiels discription, notes, year,
    def compare_other(self, value):
        if(self.description.find(value)):
            return True
        elif(self.notes.find(value)):
            return True
        elif(self.distributor.find(value)):
            return True
        else:
            return False
    #end of function
