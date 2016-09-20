#!/usr/bin/python
from media import Media

class Video(Media):
	def __init__(self, call_number, title, subjects, description, distributor, notes, series, label):
		Media.__init__(self, call_number, title, subjects, notes)
		self.call_number = call_number
		self.title = title
		self.subjects = subjects
		self.description = description
		self.distributor = distributor
		self.notes = notes
		self.series = series
		self.label = label

	def display(self):
		print "--VIDEO--"
		print "Call number- ", self.call_number
		print "Title- ", self.title
		print "Subjects- ", self.subjects
		print "Description- ", self.description
		print "Distributor- ", self.distributor
		print "Notes- ", self.notes
		print "Series- ", self.series
		print "Label- ", self.label

	def compare_other(self, word):
		val1 = self.description.find(word)
		if(val1 != -1):
			return True
		val2 = self.notes.find(word)
		if(val2 != -1):
			return True
		val3 = self.distributor.find(word)
		if(val3 != -1):
			return True
		else:
			return False
