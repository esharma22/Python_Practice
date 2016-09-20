#!/usr/bin/python

class Date:
	days = 0
	month = 0
	year = 0
	def __init__(self, days, month, year):
		self.days = days
		self.month = month
		self.year = year

	def display(self):
		print self.month, "/", self.days, "/", self.year

d1 = Date(22, 11, 1991)

d2 = Date(1, 1, 1987)

d1.display()

d2.display()
