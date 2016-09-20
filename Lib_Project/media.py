#!/usr/bin/python

class Media:
	def __init__(self, call_number, title, subjects, notes):
		self.call_number = call_number
		self.title = title
		self.subjects = subjects
		self.notes = notes

	def compare_callNum(self, word):
		val = self.call_number.find(word)
		if(val != -1):
			return True
		else:
			return False

	def compare_title(self, word):
		val = self.title.find(word)
		if(val != -1):
			return True
		else:
			return False

	def compare_subjects(self, word):
		val = self.subjects.find(word)
		if(val != -1):
			return True
		else:
			return False
