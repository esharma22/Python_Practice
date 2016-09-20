class Media:
    """Class Media"""

    #constructor
    def __init__(self, call_number, title, subjects, notes):
        self.call_number = call_number
        self.title = title
        self.subjects = subjects
        self.notes = notes
    #end of constructor

    #Function compare_callNumber
    def compare_callNumber(self, cn):
        if (self.call_number.find(cn)):
            return True
        else:
            return False
    #end of Function

    #Function to compare_title
    def compare_title(self, title):
        if (self.title.find(title)):
            return True
        else:
            return False
    #end of Function

    #Function to compare_subjects
    def compare_subjects(self, subjects):
        if (self.subjects.find(subjects)):
            return True
        else:
            return False
    #end of compare_subjects
