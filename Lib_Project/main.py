#! /usr/bin/python
from engine import Engine

def Main():
	eg = Engine()
	running = True

	while running:
		print "1- Search by call number"
		print "2- Search by title"
		print "3- Search by subjects"
		print "4- Search by other"
		choice = int(input("Select an option or enter 5 to quit- "))

		if choice == 1:
			word = str(raw_input("Enter the call number to search- "))
			print word
			result = eg.search_callNum(word)
			for i in range(len(result)):
				result[i].display()

		elif choice == 2:
			word = str(raw_input("Enter the title to search- "))
			print word
			result = eg.search_title(word)
			for i in range(len(result)):
				result[i].display()

		elif choice == 3:
			word = str(raw_input("Enter the subjects to search- "))
			print word
			result = eg.search_subjects(word)
			for i in range(len(result)):
				result[i].display()

		elif choice == 4:
			word = str(raw_input("Enter the content to search- "))
			print word
			result = eg.search_other(word)
			for i in range(len(result)):
				result[i].display()

		else:
				print "Quitting"
				running = False

if __name__ == '__main__':
	Main()
