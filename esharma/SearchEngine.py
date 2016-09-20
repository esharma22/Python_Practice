#SearchEngine class
from Book import Book
from Video import Video
from Periodic import Periodic
from Film import Film
class SearchEngine:
    """docstring for SearchEngine"""
    #Class variables
    CardCatalog = []

    #constructor
    def __init__(self):
        self.readBook()
        self.readVideo()
        self.readPeriodic()
        self.readFilm()
    #end of constructor

    #function to read Book.txt and load it into
    #card catalog
    def readBook(self):
        #open file
        file = open("book.txt", "r")
        line = file.readline()
        while line:
            fields = line.split('|')
            book = Book(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8], fields[9])
            self.CardCatalog.append(book)
            line = file.readline()
        #end of while
    #end of function

    #function to read video.txt and load it into
    #card catalog
    def readVideo(self):
        #open file
        file = open("video.txt", "r")
        line = file.readline()
        while line:
            fields = line.split('|')
            video = Video(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7])
            self.CardCatalog.append(video)
            line = file.readline()
        #end of while
    #end of function

    #function to read periodic.txt and load it into
    #card catalog
    def readPeriodic(self):
        #open file
        file = open("periodic.txt", "r")
        line = file.readline()
        while line:
            fields = line.split('|')
            periodic = Periodic(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8], fields[9], fields[10], fields[11])
            self.CardCatalog.append(periodic)
            line = file.readline()
        #end of while
    #end of function

    #function to read film.txt and load it into
    #card catalog
    def readFilm(self):
        #open file
        file = open("film.txt", "r")
        line = file.readline()
        while line:
            fields = line.split('|')
            film = Film(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5])
            self.CardCatalog.append(film)
            line = file.readline()
        #end of while
    #end of function


    #Function search by call_number
    def search_by_callNumber(self, word):
        result = []
        for count in range(len(self.CardCatalog)):
            check = self.CardCatalog[count].compare_callNumber(word)
            if (check == True):
                result.append(self.CardCatalog[count])
        #end of for

        return result;
    #end of function

    #Function search by title
    def search_by_title(self, word):
        result = []
        for count in range(len(self.CardCatalog)):
            check = self.CardCatalog[count].compare_title(word)
            if (check == True):
                result.append(self.CardCatalog[count])
        #end of for

        return result;
    #end of function

    #Function search by subjects
    def search_by_subjects(self, word):
        result = []
        for count in range(len(self.CardCatalog)):
            check = self.CardCatalog[count].compare_subjects(word)
            if (check == True):
                result.append(self.CardCatalog[count])
        #end of for

        return result;
    #end of function

    #Function search by other
    def search_by_other(self, word):
        result = []
        for count in range(len(self.CardCatalog)):
            check = self.CardCatalog[count].compare_other(word)
            if (check == True):
                result.append(self.CardCatalog[count])
        #end of for

        return result;
    #end of function
