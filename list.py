#! /usr/bin/python

a = [45, 23, 237, 2513]
b = ["Ektaa", "Sunil", "Rohan", "Nikhil"]
c = [3, 6, 1, 7, 1]

print cmp(a, c)	#Compare lists a and c

print len(b)		#Prints length of list b

print max(a)		#Prints the object with maximum value in list a

print min(c)		#Prints the object with minimum value in list c

b.append("Gangadhar")	#Appends "Gangadhar" to list b
print b

print c.count(1)	#Prints the number of times 1 appears in list c

c.extend(a)
print c				#Appends contents of list a to list c

b.insert(2, "Niranjan")
print b				#Inserts "Niranjan" into list b at index 2

a.reverse()			#Reverses elements of list a	
print a
