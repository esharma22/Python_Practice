#! /usr/bin/python

def print_str(str):
	#Simply prints string received in variable str
	print "The string to be printed:"
	print str
	return

def print_stats(name, age = 24):
	#Prints Name and age. If age is not passed then default value is 24
	print "Name- ", name
	print "Age- ",age
	return

def addition(a, b):
	c = a + b
	return c

a = "Ektaa"

print_str(a)
print_stats("Sunil", age = 28)
print_stats("Ektaa")
x = addition(23, 54)
print "Addition- ", x
