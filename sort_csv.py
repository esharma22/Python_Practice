#! /usr/bin/python
import csv
import operator

mylist = []

myFile = open("data.csv", "r")
myReader = csv.reader(myFile)

firstline = myReader.next()

for row in myReader:
	record = [row[0], row[1], row[2], float(row[3])]
	mylist.append(record)

table = sorted(mylist, key = operator.itemgetter(3))

print '{0:11} {1:35} {2:10} {3:5}'.format(firstline[0], firstline[1], firstline[2], firstline[3])
for row in table:
	print '{0:11} {1:35} {2:10} {3:5}'.format(row[0], row[1], row[2], row[3])

myFile.close()
