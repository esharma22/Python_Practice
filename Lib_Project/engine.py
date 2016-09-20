#!/usr/bin/python
from book import Book
from video import Video
from media import Media

class Engine:
	Catalog = []

	def __init__(self):
		self.read_book()
		self.read_video()

	def read_book(self):
		with open("book.txt", "r+") as f1:
			line = f1.readline()
			while line:
				fields = line.split('|')
				book = Book(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8], fields[9])
				self.Catalog.append(book)
				line = f1.readline()
		f1.close()

	def read_video(self):
		with open("video.txt", "r+") as f2:
			line = f2.readline()
			while line:
				fields = line.split('|')
				video = Video(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7])
				self.Catalog.append(video)
				line = f2.readline()
		f2.close()

	def search_callNum(self, word):
		result = []
		for i in range(len(self.Catalog)):
			check = self.Catalog[i].compare_callNum(word)
			if check == True:
				result.append(self.Catalog[i])
		return result

	def search_title(self, word):
		result = []
		for i in range(len(self.Catalog)):
			check = self.Catalog[i].compare_title(word)
			if check == True:
				result.append(self.Catalog[i])
		return result

	def search_subjects(self, word):
		result = []
		for i in range(len(self.Catalog)):
			check = self.Catalog[i].compare_subjects(word)
			if check == True:
				result.append(self.Catalog[i])
		return result

	def search_other(self, word):
		result = []
		for i in range(len(self.Catalog)):
			check = self.Catalog[i].compare_other(word)
			if check == True:
				result.append(self.Catalog[i])
		return result
