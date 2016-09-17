#! /usr/bin/python

str = raw_input("Enter your string- ")
print "Received string is- ", str

a = input("Enter first number- ")
b = input("Enter second number- ")
print "Addition is- ", a+b

f1 = open("temp.txt", "w+")
print "File name- ",f1.name
f1.write("Ektaa you wrote to a file! Yay!")
f1.seek(0,0)
myString = f1.read()
print myString
f1.close()
