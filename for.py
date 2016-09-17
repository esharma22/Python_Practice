#! /usr/bin/python

a = "Ektaa Sharma"
b = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
c = [12, 34, 1, 22, 87, 28]
d = [123, 23, 129, 458, 83984]

for letter in a:
	print "Current letter- ", letter

for day in b:
	print "Day of the week- ", day

for num in range(len(c)):
	for num2 in range(len(c)):
		if(c[num] < c[num2]):
			temp = c[num]
			c[num] = c[num2]
			c[num2] = temp
print c

d.sort()
print d
