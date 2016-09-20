#Main file, this file provides interface for user to
# to interact with
from SearchEngine import SearchEngine
def Main():
    se = SearchEngine()
    keepRunning = True

    while (keepRunning):
        print("------------------------------------------------------------")
        print("                WELCOME TO GAVELTON LIBRARY                 ")
        print("------------------------------------------------------------")
        print("1.Search by Call Number")
        print("2.Search by Title")
        print("3.Search by Subject")
        print("4.Search by Other fields (Description, Year, Series, etc.)")
        print("5.Exit")
        print("------------------------------------------------------------")
        choice = input("Enter your choice:")

        if (choice == '1'):
            word = input("Enter call number: ")
            result = se.search_by_callNumber(word)
            for count in range(len(result)):
                result[count].display()
            #end of for
        elif(choice == '2'):
            word = input("Enter title: ")
            result = se.search_by_title(word)
            for count in range(len(result)):
                result[count].display()
            #end of for
        elif(choice == '3'):
            word = input("Enter subject: ")
            result = se.search_by_subjects(word)
            for count in range(len(result)):
                result[count].display()
            #end of for
        elif(choice == '4'):
            word = input("Enter any other paramenter: ")
            result = se.search_by_other(word)
            for count in range(len(result)):
                result[count].display()
            #end of for
        elif(choice == '5'):
            print("Exiting");
            keepRunning = False
        else:
            print("ERROR: Invalid choice.")
    #end of while
#end of Main

if __name__ == '__main__':
    Main()
