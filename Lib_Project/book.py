#!/usr/bin/python
from media import Media

class Book(Media):
	def __init__(self, call_number, title, subjects, author, description, publisher, city, year, series, notes) : 
		Media.__init__(self, call_number, title, subjects, notes)
		self.call_number = call_number
		self.title = title
		self.subjects = subjects
		self.author = author
		self.description = description
		self.publisher = publisher
		self.city = city
		self.year = year
		self.series = series
		self.notes = notes

	def display(self):
		print "--BOOK--"
		print "Call number- ", self.call_number
		print "Title- ", self.title
		print "Subjects- ", self.subjects
		print "Author- ", self.author
		print "Description- ", self.description
		print "Publisher- ", self.publisher
		print "City- ", self.city
		print "Year- ", self.year
		print "Series- ", self.series
		print "Notes- ", self.notes

	def compare_other(self, word):
		val1 = self.description.find(word)
		if (val1 != -1):
			return True
		val2 = self.notes.find(word)
		if (val2 != -1):
			return True
		val3 = self.year.find(word)
		if (val3 != -1):
			return True
		else:
			return False
