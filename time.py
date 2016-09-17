#! /usr/bin/python
import time
import calendar

localtime = time.localtime(time.time())
print "Current local time- ", localtime

localtime = time.asctime(time.localtime(time.time()))
print "Formatted time- ", localtime

cal = calendar.month(2016, 4)
print "Current month"
print cal
