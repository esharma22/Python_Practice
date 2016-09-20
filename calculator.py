#!/usr/bin/python

def addition(x, y = 0):
	ans = x + y
	print "Addition is- ", ans

def subtraction(x, y = 0):
	ans = x - y
	print "Subtraction is- ", ans

def multiplication(x, y = 0):
	ans = x * y
	print "Multiplication is- ", ans

def division(x, y = 0):
	ans = x / y
	print "Division is- ", ans

run = True;
while(run):
	print("1- Addition")
	print("2- Subtraction")
	print("3- Multiplication")
	print("4- Division")
	print("5- Quit")

	choice = int(input("Select an option by entering the integer value- "))

	if choice == 1:
		print("Addition")
		a = int(input("Enter first integer- "))
		b = int(input("Enter second integer- "))
		addition(a, b)
	elif choice == 2:
		print("Subtraction")
		a = int(input("Enter first integer- "))
		b = int(input("Enter second integer- "))
		subtraction(a, b)
	elif choice == 3:
		print("Multiplication")
		a = int(input("Enter first integer- "))
		b = int(input("Enter second integer- "))
		multiplication(a, b)
	elif choice == 4:
		print("Division")
		a = int(input("Enter first integer- "))
		b = int(input("Enter second integer- "))
		division(a, b)
	else:
		print("Quitting")
		run = False;
